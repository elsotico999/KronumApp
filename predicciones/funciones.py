from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
import numpy as np
import pandas as pd
from tkinter import messagebox

df =  pd.read_csv("results.csv")
df["date"] = pd.to_datetime(df["date"])
df.isna().sum()
df.head()

df.dropna(inplace=True)
df.dtypes

df.sort_values("date").tail()
df = df[(df["date"] >= "2018-8-1")].reset_index(drop=True)
df.sort_values("date").tail()

df.home_team.value_counts()

rank = pd.read_csv("fifa_ranking-2022-12-22.csv")

rank["rank_date"] = pd.to_datetime(rank["rank_date"])

rank = rank[(rank["rank_date"] >= "2018-8-1")].reset_index(drop=True)

rank["country_full"] = rank["country_full"].str.replace("IR Iran", "Iran").str.replace("Korea Republic", "South Korea").str.replace("USA", "United States")

rank = rank.set_index(['rank_date']).groupby(['country_full'], group_keys=False).resample('D').first().fillna(method='ffill').reset_index()

df_wc_ranked = df.merge(rank[["country_full", "total_points", "previous_points", "rank", "rank_change", "rank_date"]], left_on=["date", "home_team"], right_on=["rank_date", "country_full"]).drop(["rank_date", "country_full"], axis=1)

df_wc_ranked = df_wc_ranked.merge(rank[["country_full", "total_points", "previous_points", "rank", "rank_change", "rank_date"]], left_on=["date", "away_team"], right_on=["rank_date", "country_full"], suffixes=("_home", "_away")).drop(["rank_date", "country_full"], axis=1)

df_wc_ranked[(df_wc_ranked.home_team == "Brazil") | (df_wc_ranked.away_team == "Brazil")].tail(10)

df = df_wc_ranked

def result_finder(home, away):
    if home > away:
        return pd.Series([0, 3, 0])
    if home < away:
        return pd.Series([1, 0, 3])
    else:
        return pd.Series([2, 1, 1])

results = df.apply(lambda x: result_finder(x["home_score"], x["away_score"]), axis=1)

df[["result", "home_team_points", "away_team_points"]] = results

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 10))
sns.heatmap(df[["total_points_home", "rank_home", "total_points_away", "rank_away"]].corr())
#plt.show()

df["rank_dif"] = df["rank_home"] - df["rank_away"]
df["sg"] = df["home_score"] - df["away_score"]
df["points_home_by_rank"] = df["home_team_points"]/df["rank_away"]
df["points_away_by_rank"] = df["away_team_points"]/df["rank_home"]

home_team = df[["date", "home_team", "home_score", "away_score", "rank_home", "rank_away","rank_change_home", "total_points_home", "result", "rank_dif", "points_home_by_rank", "home_team_points"]]

away_team = df[["date", "away_team", "away_score", "home_score", "rank_away", "rank_home","rank_change_away", "total_points_away", "result", "rank_dif", "points_away_by_rank", "away_team_points"]]

home_team.columns = [h.replace("home_", "").replace("_home", "").replace("away_", "suf_").replace("_away", "_suf") for h in home_team.columns]

away_team.columns = [a.replace("away_", "").replace("_away", "").replace("home_", "suf_").replace("_home", "_suf") for a in away_team.columns]

team_stats = home_team.append(away_team)

#Esta columna se utilizará para calcular las características para la simulación

team_stats_raw = team_stats.copy()

stats_val = []

for index, row in team_stats.iterrows():
    team = row["team"]
    date = row["date"]
    past_games = team_stats.loc[(team_stats["team"] == team) & (team_stats["date"] < date)].sort_values(by=['date'], ascending=False)
    last5 = past_games.head(5)
    
    goals = past_games["score"].mean()
    goals_l5 = last5["score"].mean()
    
    goals_suf = past_games["suf_score"].mean()
    goals_suf_l5 = last5["suf_score"].mean()
    
    rank = past_games["rank_suf"].mean()
    rank_l5 = last5["rank_suf"].mean()
    
    if len(last5) > 0:
        points = past_games["total_points"].values[0] - past_games["total_points"].values[-1]#qtd de pontos ganhos
        points_l5 = last5["total_points"].values[0] - last5["total_points"].values[-1] 
    else:
        points = 0
        points_l5 = 0
        
    gp = past_games["team_points"].mean()
    gp_l5 = last5["team_points"].mean()
    
    gp_rank = past_games["points_by_rank"].mean()
    gp_rank_l5 = last5["points_by_rank"].mean()
    
    stats_val.append([goals, goals_l5, goals_suf, goals_suf_l5, rank, rank_l5, points, points_l5, gp, gp_l5, gp_rank, gp_rank_l5])

stats_cols = ["goals_mean", "goals_mean_l5", "goals_suf_mean", "goals_suf_mean_l5", "rank_mean", "rank_mean_l5", "points_mean", "points_mean_l5", "game_points_mean", "game_points_mean_l5", "game_points_rank_mean", "game_points_rank_mean_l5"]

stats_df = pd.DataFrame(stats_val, columns=stats_cols)

full_df = pd.concat([team_stats.reset_index(drop=True), stats_df], axis=1, ignore_index=False)

home_team_stats = full_df.iloc[:int(full_df.shape[0]/2),:]
away_team_stats = full_df.iloc[int(full_df.shape[0]/2):,:]

home_team_stats.columns[-12:]

home_team_stats = home_team_stats[home_team_stats.columns[-12:]]
away_team_stats = away_team_stats[away_team_stats.columns[-12:]]

home_team_stats.columns = ['home_'+str(col) for col in home_team_stats.columns]
away_team_stats.columns = ['away_'+str(col) for col in away_team_stats.columns]

match_stats = pd.concat([home_team_stats, away_team_stats.reset_index(drop=True)], axis=1, ignore_index=False)

full_df = pd.concat([df, match_stats.reset_index(drop=True)], axis=1, ignore_index=False)

full_df.columns

#se cuantifica la importancia del juego creando una columna que encuentra la competencia de dicho juego.

def find_friendly(x):
    if x == "Friendly":
        return 1
    else: return 0

full_df["is_friendly"] = full_df["tournament"].apply(lambda x: find_friendly(x)) 

full_df = pd.get_dummies(full_df, columns=["is_friendly"])

full_df.columns

base_df = full_df[["date", "home_team", "away_team", "rank_home", "rank_away","home_score", "away_score","result", "rank_dif", "rank_change_home", "rank_change_away", 'home_goals_mean',
       'home_goals_mean_l5', 'home_goals_suf_mean', 'home_goals_suf_mean_l5',
       'home_rank_mean', 'home_rank_mean_l5', 'home_points_mean',
       'home_points_mean_l5', 'away_goals_mean', 'away_goals_mean_l5',
       'away_goals_suf_mean', 'away_goals_suf_mean_l5', 'away_rank_mean',
       'away_rank_mean_l5', 'away_points_mean', 'away_points_mean_l5','home_game_points_mean', 'home_game_points_mean_l5',
       'home_game_points_rank_mean', 'home_game_points_rank_mean_l5','away_game_points_mean',
       'away_game_points_mean_l5', 'away_game_points_rank_mean',
       'away_game_points_rank_mean_l5',
       'is_friendly_0', 'is_friendly_1']]

base_df.tail()

base_df.isna().sum()

base_df_no_fg = base_df.dropna()

df = base_df_no_fg

def no_draw(x):
    if x == 2:
        return 1
    else:
        return x
    
df["target"] = df["result"].apply(lambda x: no_draw(x))

data1 = df[list(df.columns[8:20].values) + ["target"]]
data2 = df[df.columns[20:]]

scaled = (data1[:-1] - data1[:-1].mean()) / data1[:-1].std()
scaled["target"] = data1["target"]
violin1 = pd.melt(scaled,id_vars="target", var_name="features", value_name="value")

scaled = (data2[:-1] - data2[:-1].mean()) / data2[:-1].std()
scaled["target"] = data2["target"]
violin2 = pd.melt(scaled,id_vars="target", var_name="features", value_name="value")

plt.figure(figsize=(15,10))
sns.violinplot(x="features", y="value", hue="target", data=violin1,split=True, inner="quart")
plt.xticks(rotation=90)
#plt.show()

plt.figure(figsize=(15,10))
sns.violinplot(x="features", y="value", hue="target", data=violin2,split=True, inner="quart")
plt.xticks(rotation=90)
#plt.show()

dif = df.copy()

dif.loc[:, "goals_dif"] = dif["home_goals_mean"] - dif["away_goals_mean"]
dif.loc[:, "goals_dif_l5"] = dif["home_goals_mean_l5"] - dif["away_goals_mean_l5"]
dif.loc[:, "goals_suf_dif"] = dif["home_goals_suf_mean"] - dif["away_goals_suf_mean"]
dif.loc[:, "goals_suf_dif_l5"] = dif["home_goals_suf_mean_l5"] - dif["away_goals_suf_mean_l5"]
dif.loc[:, "goals_made_suf_dif"] = dif["home_goals_mean"] - dif["away_goals_suf_mean"]
dif.loc[:, "goals_made_suf_dif_l5"] = dif["home_goals_mean_l5"] - dif["away_goals_suf_mean_l5"]
dif.loc[:, "goals_suf_made_dif"] = dif["home_goals_suf_mean"] - dif["away_goals_mean"]
dif.loc[:, "goals_suf_made_dif_l5"] = dif["home_goals_suf_mean_l5"] - dif["away_goals_mean_l5"]

data_difs = dif.iloc[:, -8:]
scaled = (data_difs - data_difs.mean()) / data_difs.std()
scaled["target"] = data2["target"]
violin = pd.melt(scaled,id_vars="target", var_name="features", value_name="value")

plt.figure(figsize=(10,10))
sns.violinplot(x="features", y="value", hue="target", data=violin,split=True, inner="quart")
plt.xticks(rotation=90)
#plt.show()

dif.loc[:, "dif_points"] = dif["home_game_points_mean"] - dif["away_game_points_mean"]

dif.loc[:, "dif_points_l5"] = dif["home_game_points_mean_l5"] - dif["away_game_points_mean_l5"]

dif.loc[:, "dif_points_rank"] = dif["home_game_points_rank_mean"] - dif["away_game_points_rank_mean"]

dif.loc[:, "dif_points_rank_l5"] = dif["home_game_points_rank_mean_l5"] - dif["away_game_points_rank_mean_l5"]

dif.loc[:, "dif_rank_agst"] = dif["home_rank_mean"] - dif["away_rank_mean"]

dif.loc[:, "dif_rank_agst_l5"] = dif["home_rank_mean_l5"] - dif["away_rank_mean_l5"]

dif.loc[:, "goals_per_ranking_dif"] = (dif["home_goals_mean"] / dif["home_rank_mean"]) - (dif["away_goals_mean"] / dif["away_rank_mean"])

dif.loc[:, "goals_per_ranking_suf_dif"] = (dif["home_goals_suf_mean"] / dif["home_rank_mean"]) - (dif["away_goals_suf_mean"] / dif["away_rank_mean"])

dif.loc[:, "goals_per_ranking_dif_l5"] = (dif["home_goals_mean_l5"] / dif["home_rank_mean"]) - (dif["away_goals_mean_l5"] / dif["away_rank_mean"])

dif.loc[:, "goals_per_ranking_suf_dif_l5"] = (dif["home_goals_suf_mean_l5"] / dif["home_rank_mean"]) - (dif["away_goals_suf_mean_l5"] / dif["away_rank_mean"])

data_difs = dif.iloc[:, -10:]
scaled = (data_difs - data_difs.mean()) / data_difs.std()
scaled["target"] = data2["target"]
violin = pd.melt(scaled,id_vars="target", var_name="features", value_name="value")

plt.figure(figsize=(15,10))
sns.violinplot(x="features", y="value", hue="target", data=violin,split=True, inner="quart")
plt.xticks(rotation=90)
#plt.show()

plt.figure(figsize=(15,10))
sns.boxplot(x="features", y="value", hue="target", data=violin)
plt.xticks(rotation=90)
#plt.show()

sns.jointplot(data = data_difs, x = 'goals_per_ranking_dif', y = 'goals_per_ranking_dif_l5', kind="reg")
#plt.show()

sns.jointplot(data = data_difs, x = 'dif_rank_agst', y = 'dif_rank_agst_l5', kind="reg")
#plt.show()

sns.jointplot(data = data_difs, x = 'dif_points', y = 'dif_points_l5', kind="reg")
#plt.show()

sns.jointplot(data = data_difs, x = 'dif_points_rank', y = 'dif_points_rank_l5', kind="reg")
#plt.show()

def create_db(df):
    columns = ["home_team", "away_team", "target", "rank_dif", "home_goals_mean", "home_rank_mean", "away_goals_mean", "away_rank_mean", "home_rank_mean_l5", "away_rank_mean_l5", "home_goals_suf_mean", "away_goals_suf_mean", "home_goals_mean_l5", "away_goals_mean_l5", "home_goals_suf_mean_l5", "away_goals_suf_mean_l5", "home_game_points_rank_mean", "home_game_points_rank_mean_l5", "away_game_points_rank_mean", "away_game_points_rank_mean_l5","is_friendly_0", "is_friendly_1"]
    
    base = df.loc[:, columns]
    base.loc[:, "goals_dif"] = base["home_goals_mean"] - base["away_goals_mean"]
    base.loc[:, "goals_dif_l5"] = base["home_goals_mean_l5"] - base["away_goals_mean_l5"]
    base.loc[:, "goals_suf_dif"] = base["home_goals_suf_mean"] - base["away_goals_suf_mean"]
    base.loc[:, "goals_suf_dif_l5"] = base["home_goals_suf_mean_l5"] - base["away_goals_suf_mean_l5"]
    base.loc[:, "goals_per_ranking_dif"] = (base["home_goals_mean"] / base["home_rank_mean"]) - (base["away_goals_mean"] / base["away_rank_mean"])
    base.loc[:, "dif_rank_agst"] = base["home_rank_mean"] - base["away_rank_mean"]
    base.loc[:, "dif_rank_agst_l5"] = base["home_rank_mean_l5"] - base["away_rank_mean_l5"]
    base.loc[:, "dif_points_rank"] = base["home_game_points_rank_mean"] - base["away_game_points_rank_mean"]
    base.loc[:, "dif_points_rank_l5"] = base["home_game_points_rank_mean_l5"] - base["away_game_points_rank_mean_l5"]
    
    model_df = base[["home_team", "away_team", "target", "rank_dif", "goals_dif", "goals_dif_l5", "goals_suf_dif", "goals_suf_dif_l5", "goals_per_ranking_dif", "dif_rank_agst", "dif_rank_agst_l5", "dif_points_rank", "dif_points_rank_l5", "is_friendly_0", "is_friendly_1"]]
    return model_df

model_db = create_db(df)

model_db

X = model_db.iloc[:, 3:]
y = model_db[["target"]]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=1)

gb = GradientBoostingClassifier(random_state=5)

params = {"learning_rate": [0.01, 0.1, 0.5],
            "min_samples_split": [5, 10],
            "min_samples_leaf": [3, 5],
            "max_depth":[3,5,10],
            "max_features":["sqrt"],
            "n_estimators":[100, 200]
         } 

gb_cv = GridSearchCV(gb, params, cv = 3, n_jobs = -1, verbose = False)

gb_cv.fit(X_train.values, np.ravel(y_train))

gb = gb_cv.best_estimator_
gb

params_rf = {"max_depth": [20],
                "min_samples_split": [10],
                "max_leaf_nodes": [175],
                "min_samples_leaf": [5],
                "n_estimators": [250],
                 "max_features": ["sqrt"],
                }

rf = RandomForestClassifier(random_state=1)

rf_cv = GridSearchCV(rf, params_rf, cv = 3, n_jobs = -1, verbose = False)

rf_cv.fit(X_train.values, np.ravel(y_train))

rf = rf_cv.best_estimator_

from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score

def analyze(model):
    fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test.values)[:,1]) #test AUC
    plt.figure(figsize=(15,10))
    plt.plot([0, 1], [0, 1], 'k--')
    plt.plot(fpr, tpr, label="test")

    fpr_train, tpr_train, _ = roc_curve(y_train, model.predict_proba(X_train.values)[:,1]) #train AUC
    plt.plot(fpr_train, tpr_train, label="train")
    auc_test = roc_auc_score(y_test, model.predict_proba(X_test.values)[:,1])
    auc_train = roc_auc_score(y_train, model.predict_proba(X_train.values)[:,1])
    plt.legend()
    plt.title('AUC score is %.2f on test and %.2f on training'%(auc_test, auc_train))
    #plt.show()
    
    plt.figure(figsize=(15, 10))
    cm = confusion_matrix(y_test, model.predict(X_test.values))
    #sns.heatmap(cm, annot=True, fmt="d")
    
analyze(gb)

analyze(rf)

from operator import itemgetter


def find_stats(team_1):
    #team_1 = "Qatar"
        past_games = team_stats_raw[(team_stats_raw["team"] == team_1)].sort_values("date")
        last5 = team_stats_raw[(team_stats_raw["team"] == team_1)].sort_values("date").tail(5)

        team_1_rank = past_games["rank"].values[-1]
        team_1_goals = past_games.score.mean()
        team_1_goals_l5 = last5.score.mean()
        team_1_goals_suf = past_games.suf_score.mean()
        team_1_goals_suf_l5 = last5.suf_score.mean()
        team_1_rank_suf = past_games.rank_suf.mean()
        team_1_rank_suf_l5 = last5.rank_suf.mean()
        team_1_gp_rank = past_games.points_by_rank.mean()
        team_1_gp_rank_l5 = last5.points_by_rank.mean()

        return [team_1_rank, team_1_goals, team_1_goals_l5, team_1_goals_suf, team_1_goals_suf_l5, team_1_rank_suf, team_1_rank_suf_l5, team_1_gp_rank, team_1_gp_rank_l5]
    
def find_features(team_1, team_2):
        rank_dif = team_1[0] - team_2[0]
        goals_dif = team_1[1] - team_2[1]
        goals_dif_l5 = team_1[2] - team_2[2]
        goals_suf_dif = team_1[3] - team_2[3]
        goals_suf_dif_l5 = team_1[4] - team_2[4]
        goals_per_ranking_dif = (team_1[1]/team_1[5]) - (team_2[1]/team_2[5])
        dif_rank_agst = team_1[5] - team_2[5]
        dif_rank_agst_l5 = team_1[6] - team_2[6]
        dif_gp_rank = team_1[7] - team_2[7]
        dif_gp_rank_l5 = team_1[8] - team_2[8]
    
        return [rank_dif, goals_dif, goals_dif_l5, goals_suf_dif, goals_suf_dif_l5, goals_per_ranking_dif, dif_rank_agst, dif_rank_agst_l5, dif_gp_rank, dif_gp_rank_l5, 1, 0]

size = (50, 50)

# lista de banderas de los países
banderas = {
    "Afghanistan": "af.png",
  "Albania": "al.png",
  "Algeria": "dz.png",
  "Andorra": "ad.png",
  "Angola": "ao.png",
  "Antigua and Barbuda": "ag.png",
  "Argentina": "ar.png",
  "Armenia": "am.png",
  "Australia": "au.png",
  "Austria": "at.png",
  "Azerbaijan": "az.png",
  "Bahamas": "bs.png",
  "Bahrain": "bh.png",
  "Bangladesh": "bd.png",
  "Barbados": "bb.png",
  "Belarus": "by.png",
  "Belgium": "be.png",
  "Belize": "bz.png",
  "Benin": "bj.png",
  "Bhutan": "bt.png",
  "Bolivia": "bo.png",
  "Bosnia and Herzegovina": "ba.png",
  "Botswana": "bw.png",
  "Brazil": "br.png",
  "Brunei": "bn.png",
  "Bulgaria": "bg.png",
  "Burkina Faso": "bf.png",
  "Burundi": "bi.png",
  "Cabo Verde": "cv.png",
  "Cambodia": "kh.png",
  "Cameroon": "cm.png",
  "Canada": "ca.png",
  "Central African Republic": "cf.png",
  "Chad": "td.png",
  "Chile": "cl.png",
  "China": "cn.png",
  "Colombia": "co.png",
  "Comoros": "km.png",
  "Congo, Democratic Republic of the": "cd.png",
  "Congo, Republic of the": "cg.png",
  "Costa Rica": "cr.png",
  "Côte d'Ivoire": "ci.png",
  "Croatia": "hr.png",
  "Cuba": "cu.png",
  "Cyprus": "cy.png",
  "Czech Republic": "cz.png",
  "Denmark": "dk.png",
  "Djibouti": "dj.png",
  "Dominica": "dm.png",
  "Dominican Republic": "do.png",
  "Ecuador": "ec.png",
  "Egypt": "eg.png",
  "El Salvador": "sv.png",
  "Equatorial Guinea": "gq.png",
  "Eritrea": "er.png",
  "Estonia": "ee.png",
  "Eswatini": "sz.png",
  "Ethiopia": "et.png",
  "Fiji": "fj.png",
  "Finland": "fi.png",
  "France": "fr.png",
  "Gabon": "ga.png",
  "Gambia": "gm.png",
  "Georgia": "ge.png",
  "Germany": "de.png",
  "Ghana": "gh.png",
  "Greece": "gr.png",
  "Grenada": "gd.png",
  "Guatemala": "gt.png",
  "Guinea": "gn.png",
  "Guinea-Bissau": "gw.png",
  "Guyana": "gy.png",
  "Haiti": "ht.png",
  "Honduras": "hn.png",
  "Hungary": "hu.png",
  "Iceland": "is.png",
  "India": "in.png",
  "Indonesia": "id.png",
  "Iran": "ir.png",
  "Iraq": "iq.png",
  "Ireland": "ie.png",
  "Israel": "il.png",
  "Italy": "it.png",
  "Jamaica": "jm.png",
  "Japan": "jp.png",
  "Jordan": "jo.png",
  "Kazakhstan": "kz.png",
  "Kenya": "ke.png",
  "Kiribati": "ki.png",
  "Kosovo": "xk.png",
  "Kuwait": "kw.png",
  "Kyrgyzstan": "kg.png",
  "Laos": "la.png",
  "Latvia": "lv.png",
  "Lebanon": "lb.png",
  "Lesotho": "ls.png",
  "Liberia": "lr.png",
  "Libya": "ly.png",
  "Liechtenstein": "li.png",
  "Lithuania": "lt.png",
  "Luxembourg": "lu.png",
  "Madagascar": "mg.png",
  "Malawi": "mw.png",
  "Malaysia": "my.png",
  "Maldives": "mv.png",
  "Mali": "ml.png",
  "Malta": "mt.png",
  "Marshall Islands": "mh.png",
  "Mauritania": "mr.png",
  "Mauritius": "mu.png",
  "Mexico": "mx.png",
  "Micronesia": "fm.png",
  "Moldova": "md.png",
  "Monaco": "mc.png",
  "Mongolia": "mn.png",
  "Montenegro": "me.png",
  "Morocco": "ma.png",
  "Mozambique": "mz.png",
  "Myanmar": "mm.png",
  "Namibia": "na.png",
  "Nauru": "nr.png",
  "Nepal": "np.png",
  "Netherlands": "nl.png",
  "New Zealand": "nz.png",
  "Nicaragua": "ni.png",
  "Niger": "ne.png",
  "Nigeria": "ng.png",
  "North Korea": "kp.png",
  "North Macedonia": "mk.png",
  "Norway": "no.png",
  "Oman": "om.png",
  "Pakistan": "pk.png",
  "Palau": "pw.png",
  "Palestine": "ps.png",
  "Panama": "pa.png",
  "Papua New Guinea": "pg.png",
  "Paraguay": "py.png",
  "Peru": "pe.png",
  "Philippines": "ph.png",
  "Poland": "pl.png",
  "Portugal": "pt.png",
  "Qatar": "qa.png",
  "Romania": "ro.png",
  "Russia": "ru.png",
  "Rwanda": "rw.png",
  "Saint Kitts and Nevis": "kn.png",
  "Saint Lucia": "lc.png",
  "Saint Vincent and the Grenadines": "vc.png",
  "Samoa": "ws.png",
  "San Marino": "sm.png",
  "Sao Tome and Principe": "st.png",
  "Saudi Arabia": "sa.png",
  "Senegal": "sn.png",
  "Serbia": "rs.png",
  "Seychelles": "sc.png",
  "Sierra Leone": "sl.png",
  "Singapore": "sg.png",
  "Slovakia": "sk.png",
  "Slovenia": "si.png",
  "Solomon Islands": "sb.png",
  "Somalia": "so.png",
  "South Africa": "za.png",
  "South Korea": "kr.png",
  "South Sudan": "ss.png",
  "Spain": "es.png",
  "Sri Lanka": "lk.png",
  "Sudan": "sd.png",
  "Suriname": "sr.png",
  "Sweden": "se.png",
  "Switzerland": "ch.png",
  "Syria": "sy.png",
  "Taiwan": "tw.png",
  "Tajikistan": "tj.png",
  "Tanzania": "tz.png",
  "Thailand": "th.png",
  "Timor-Leste": "tl.png",
  "Togo": "tg.png",
  "Tonga": "to.png",
  "Trinidad and Tobago": "tt.png",
  "Tunisia": "tn.png",
  "Turkey": "tr.png",
  "Turkmenistan": "tm.png",
  "Tuvalu": "tv.png",
  "Uganda": "ug.png",
  "Ukraine": "ua.png",
  "United Arab Emirates": "ae.png",
  "United Kingdom": "gb.png",
  "United States of America": "us.png",
  "Uruguay": "uy.png",
  "Uzbekistan": "uz.png",
  "Vanuatu": "vu.png",
  "Vatican City": "va.png",
  "Venezuela": "ve.png",
  "Vietnam": "vn.png",
  "Yemen": "ye.png",
  "Zambia": "zm.png",
  "Zimbabwe": "zw.png"
}
