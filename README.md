# downdetector_zbx_grafana

### Requerimentos
```
Python 3
beautifulsoup4
cloudscraper
openssl 1.1.1
```

### Uso
```
./downdetector.py {nome site}
./downdetector.py whatsapp

```

#### Debian /Ubuntu ####
<pre>apt install python3-pip
pip3 install beautifulsoup4
pip3 install cloudscraper</pre>

Caso já tenha o pip instalado e queira instalar as dependencias rode:
```
pip3 install requirements.txt
```

Copie os arquivos downdetectorDiscovery.py downdetectorlist.list downdetector.py para /usr/lib/zabbix/externalscripts, altere suas permissões para o usuários zabbix. 
<pre>chown zabbix. /usr/lib/zabbix/externalscripts/downdetector*
chmod a+x /usr/lib/zabbix/externalscripts/downdetector*.py</pre>


## Discovery/Auto Configuração

Edite o arquivo downdetectorlist.list e altere para 1 os sites/host que deseja monitorar.

#### downdetectordiscoverylist.list
```
0 INATIVO
1 ATIVO

0;caixa;Caixa Econômica Federal
1;caixa;Caixa Econômica Federal
```
