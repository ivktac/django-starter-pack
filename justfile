export VIRTUAL_ENV := `echo ${VIRTUAL_ENV:-.venv}`
export BIN := VIRTUAL_ENV + if os_family() == "unix" { "/bin" } else { "/Scripts" }
export PIP := BIN + if os_family() == "unix" { "/python -m pip" } else { "/python.exe -m pip" }

export DEFAULT_PYTHON := if os_family() == "unix" { "python3" } else { "python" }

# List available commnads
@_default:
	@"{{ just_executable() }}" --list

# Clean up temporary files
@clean:
	rm -rf .venv

# Ensure valid virtualenv
@venv:
	#!/usr/bin/env bash
	set -euo pipefail

	# Allow users to specify python version in .env
	PYTHON_VERSION=${PYTHON_VERSION:-$DEFAULT_PYTHON}

	# Create venv and upgrade pip
	test -d $VIRTUAL_ENV || { $PYTHON_VERSION -m venv $VIRTUAL_ENV && $PIP install --upgrade pip pip-tools; }

	# Bootstrap
	$PIP install --upgrade --requirement requirements.txt

# Start virtualenv
@env-start:
	source $BIN/activate

@server: env-start
	$BIN/python backend/manage.py runserver 8000

@requests: env-start
	# $BIN/python py_client/basic.py
	# $BIN/python py_client/detail.py
	# $BIN/python py_client/create.py
	# $BIN/python py_client/list.py
	# $BIN/python py_client/update.py
	# $BIN/python py_client/delete.py
