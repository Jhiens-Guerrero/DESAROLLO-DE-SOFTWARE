.PHONY: run test

# Levantar la aplicación con variables de entorno
run:
	PORT=8080 MESSAGE="Hola CC3S2" RELEASE="v1" python3 app.py

# Probar la aplicación con curl y mostrar puertos
test:
	curl -v http://127.0.0.1:8080/
	curl -i -X POST http://127.0.0.1:8080/
	ss -ltnp | grep :8080






