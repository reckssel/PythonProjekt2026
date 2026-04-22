# Port Checker

Ein einfacher Port-Checker mit Python und wxPython.

## Beschreibung

Dieses Projekt ist ein Desktop-Tool, mit dem überprüft werden kann, ob bestimmte Ports auf einer IP-Adresse oder Domain offen sind.

Das Programm kann zum Beispiel genutzt werden, um typische Dienste wie SSH, HTTP, HTTPS, FTP oder Minecraft-Server zu testen.

Die Oberfläche wird mit wxPython erstellt.

## Funktionen

* Eingabe einer IP-Adresse oder Domain
* Eingabe eines einzelnen Ports oder eines Portbereichs
* Prüfen, ob Ports offen oder geschlossen sind
* Anzeige der Ergebnisse in einer Tabelle
* Unterstützung für bekannte Standardports
* Möglichkeit, mehrere Ports gleichzeitig zu prüfen
* Einfache und übersichtliche GUI mit wxPython

## Beispiel

IP-Adresse oder Domain:

```text
google.com
```

Ports:

```text
22, 80, 443, 25565
```

Beispielausgabe:

```text
Port 22: geschlossen
Port 80: offen
Port 443: offen
Port 25565: geschlossen
```

## Verwendete Technologien

* Python 3
* wxPython
* socket-Modul
* threading-Modul

## Installation

Repository klonen:

```bash
git clone https://github.com/reckssel/PythonProjekt2026.git
cd PythonProjekt2026
```

Abhängigkeiten installieren:

```bash
pip install wxPython
```

## Starten

```bash
python main.py
```

## Mögliche Erweiterungen

* Export der Ergebnisse als TXT oder CSV
* Verlauf der letzten Scans speichern
* Farbliche Markierung für offene und geschlossene Ports
* Unterstützung für UDP-Ports
* Multi-Threading für schnellere Scans
* Netzwerk-Scan für mehrere Geräte gleichzeitig
* Anzeige bekannter Dienste hinter Ports
* Dark Mode

## Bekannte Standardports

| Port  | Dienst    |
| ----- | --------- |
| 20    | FTP Data  |
| 21    | FTP       |
| 22    | SSH       |
| 23    | Telnet    |
| 25    | SMTP      |
| 53    | DNS       |
| 80    | HTTP      |
| 110   | POP3      |
| 143   | IMAP      |
| 443   | HTTPS     |
| 3306  | MySQL     |
| 3389  | RDP       |
| 25565 | Minecraft |

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
