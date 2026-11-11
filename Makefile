.PHONY: sockets-demo lab-up lab-down monitoring-up lint
sockets-demo:
	python3 sockets/python/tcp_chat_server.py
lab-up:
	cd lab-4g5g && docker compose up -d
lab-down:
	cd lab-4g5g && docker compose down
monitoring-up:
	cd monitoring && docker compose up -d
lint:
	python3 -m py_compile sockets/python/*.py
	shellcheck lab-4g5g/scripts/*.sh mesh/openwrt/scripts/*.sh || true
