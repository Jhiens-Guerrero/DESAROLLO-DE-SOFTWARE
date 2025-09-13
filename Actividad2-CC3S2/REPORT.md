# Actividad 2 – HTTP, DNS, TLS y 12-Factor
---
# 1) HTTP: Fundamentos y herramientas
## 1 Levantar la aplicación
(venv) jhiens@DESKTOP-5DDQDMB:~/Actividad2-CC3S2$ PORT=8080 MESSAGE="Hola CC3S2" RELEASE="v1" python3 app.py
Starting app on port 8080...
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://172.17.170.131:8080
Press CTRL+C to quit
---
## 2 Inspeccion HTTP con curl
jhiens@DESKTOP-5DDQDMB:~$  curl -v http://127.0.0.1:8080/
*   Trying 127.0.0.1:8080...
* Connected to 127.0.0.1 (127.0.0.1) port 8080
> GET / HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: Werkzeug/3.1.3 Python/3.12.3
< Date: Fri, 12 Sep 2025 21:39:55 GMT
< Content-Type: application/json
< Content-Length: 40
< Connection: close
<
{"message":"Hola CC3S2","release":"v1"}
* Closing connection


jhiens@DESKTOP-5DDQDMB:~$ curl -v http://127.0.0.1:8080/0/
*   Trying 127.0.0.1:8080...
* Connected to 127.0.0.1 (127.0.0.1) port 8080
> GET /0/ HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/1.1 404 NOT FOUND
< Server: Werkzeug/3.1.3 Python/3.12.3
< Date: Fri, 12 Sep 2025 21:41:03 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 207
< Connection: close
<
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
* Closing connection


## 3 Puertos abiertos con ss:

jhiens@DESKTOP-5DDQDMB:~$ ss -ltnp | grep :8080
LISTEN 0      128           0.0.0.0:8080      0.0.0.0:*    users:(("python3",pid=2306,fd=3))
jhiens@DESKTOP-5DDQDMB:~$

# 2) DNS: nombres, registros y caché




## Documentando diferencias:
### Diferencias usando WSL

1. **IP y puertos**
   - En Linux nativo: la app escucha en `127.0.0.1` y todos los puertos asignados directamente.  
   - En WSL: la app también escucha en `127.0.0.1`, pero los puertos están accesibles desde Windows. Esto permite probar `curl` desde Windows o desde WSL sin problemas.

2. **Comandos del sistema**
   - Linux nativo: todos los comandos (`ss`, `curl`, `lsof`) funcionan con privilegios normales o root según necesidad.  
   - WSL: la mayoría funciona igual, pero algunos comandos que requieren kernel completo (por ejemplo `iptables`, `journalctl`) pueden no funcionar o necesitar permisos especiales.

3. **Archivos y rutas**
   - Linux nativo: rutas `/home/usuario/...` funcionan normalmente.  
   - WSL: debes acceder a archivos de Windows a través de `/mnt/c/...`, pero tu proyecto en Linux (home de WSL) funciona igual.

4. **Recomendación para esta práctica**
   - Usar `127.0.0.1:8080` y `curl` funciona igual en WSL.  
   - Para ver puertos abiertos se puede usar `ss -ltnp` dentro de WSL; si quieres ver procesos desde Windows, necesitarías herramientas de Windows.




