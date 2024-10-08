#!/bin/bash
set -e

rm -rf bottlecapdave_homeassistant_eon_next
mkdir bottlecapdave_homeassistant_eon_next
cd bottlecapdave_homeassistant_eon_next
wget https://raw.githubusercontent.com/BottlecapDave/HomeAssistant-OctopusEnergy/main/home_pro_server/oeha_server.py
chmod +x oeha_server.py
wget https://raw.githubusercontent.com/BottlecapDave/HomeAssistant-OctopusEnergy/main/home_pro_server/start_server.sh
chmod +x start_server.sh
