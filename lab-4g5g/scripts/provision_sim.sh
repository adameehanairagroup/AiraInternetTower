#!/usr/bin/env bash
# Adds a TEST subscriber. Requires open5gs-dbctl and MongoDB running.
# Never commit real SIM keys.
set -euo pipefail
IMSI=${IMSI:-001010123456780}
KI=${KI:-00112233445566778899aabbccddeeff}
OPC=${OPC:-63BFA50EE6523365FF14C1F45F88737D}
open5gs-dbctl add "$IMSI" "$KI" "$OPC"
open5gs-dbctl showall
