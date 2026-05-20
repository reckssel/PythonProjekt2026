# ---- Farben (als Tupel, damit kein wx.App nötig beim Import) ----
COLOR_PORT_OPEN   = (180, 255, 180)
COLOR_PORT_CLOSED = (255, 180, 180)

# ---- Fenstergröße ----
WINDOW_SIZE = (600, 700)

# ---- Grid Spaltenbreiten ----
COL_WIDTH_PORT    = 70
COL_WIDTH_STATUS  = 100
COL_WIDTH_HOST    = 150
COL_WIDTH_TIME    = 100

# ---- Abstände ----
PADDING_SMALL  = 3
PADDING_MEDIUM = 5
PADDING_LARGE  = 10

# ---- Ports ----
DEFAULT_PORTS = [
    ("SSH",       22),
    ("HTTP",      80),
    ("HTTPS",     443),
    ("FTP",       21),
    ("SMTP",      25),
    ("DNS",       53),
    ("IMAP",      143),
    ("POP3",      110),
    ("DHCP",      67),
    ("DHCPv6",    68),
    ("Minecraft", 25565),
    ("Hytale",    5520),
    ("Proxmox",   8006),
]