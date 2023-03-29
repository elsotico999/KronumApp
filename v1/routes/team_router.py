from fastapi import APIRouter, Depends, Body, Query, Path
from fastapi import status
from typing  import List, Optional
from ..schema import team_schema
from ..service import team_service
