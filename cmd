PYTHONPATH=$(pwd) pytest tests/


#WINDOWS
$env:PYTHONPATH = (Get-Location).Path
pytest tests/
