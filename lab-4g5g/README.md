# lab-4g5g (LAB ONLY)
**Do not radiate on licensed bands.** Use ZMQ virtual radio (no RF at all) or SDR + cable + attenuators
in a shielded box. PLMN 001/01 is the test network code.

## Option A: no radio at all (recommended first)
srsRAN supports ZeroMQ virtual radio: eNB and srsUE run on one PC, talking over TCP sockets.
1. `docker compose up -d` (Open5GS core)
2. `scripts/provision_sim.sh` (add test subscriber)
3. `scripts/setup_nat.sh` (give UEs internet through your PC)
4. Run `srsenb srsran/enb.conf` then `srsue srsran/ue.conf` (install srsRAN_4G first)

## Option B: SDR + real phone (shielded box/cable, programmable SIM)
Change device_name to uhd/soapy, add attenuators, keep TX power minimal, band per your licence.

> Config files are templates. Cross-check option names with the version of srsRAN/Open5GS you install.
