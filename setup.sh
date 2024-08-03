#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define color codes for better readability
GREEN='\033[0;32m'
RED='\033[0;31m'
NO_COLOR='\033[0m'

# Log success messages
function log_success {
    echo -e "${GREEN}$1${NO_COLOR}"
}

# Log error messages and exit script
function log_error {
    echo -e "${RED}$1${NO_COLOR}" >&2
    exit 1
}

# download the files
log_success "Downloading the emulator files..."
curl -L https://github.com/Aask42/iwp_animation_emulator/archive/refs/heads/main.zip > iwp_emulator.zip || log_error "Failed to download emulator files."

# unpack the zip file
log_success "Unpacking the emulator files..."
unzip iwp_emulator.zip || log_error "Failed to unzip emulator files."

# move into the extracted directory
log_success "Moving into the extracted directory..."
cd iwp_animation_emulator-main || log_error "Failed to change directory."

# install virtualenv if you don't have it
if ! python -m pip show virtualenv &> /dev/null; then
    log_success "Installing virtualenv..."
    python -m pip install virtualenv || log_error "Failed to install virtualenv."
else
    log_success "virtualenv is already installed."
fi

# create a virtual environment
log_success "Creating a virtual environment..."
python -m venv venv || log_error "Failed to create a virtual environment."

# source your virtual environment
log_success "Activating the virtual environment..."
. ./venv/bin/activate || log_error "Failed to activate the virtual environment."

# install pygame
log_success "Installing pygame..."
pip install pygame || log_error "Failed to install pygame."

# open in vscode
log_success "Opening the project in VSCode..."
code . || log_error "Failed to open VSCode. Make sure you have VSCode installed and it's in your PATH."

# Debug instructions
log_success "Setup complete."
log_success "Debug: Open main.py and hit F5 in VSCode to start debugging."

# Make the script executable:
# chmod +x setup_emulator.sh

# Run the script:
# ./setup_emulator.sh