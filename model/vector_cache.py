
import os,pickle
from scipy import sparse
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE=os.path.join(BASE,'data','datasets','cache')
os.makedirs(CACHE,exist_ok=True)
