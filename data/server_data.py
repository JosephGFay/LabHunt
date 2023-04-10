import socket

websites = {
    "Google": "www.google.com",
    "Facebook": "www.facebook.com",
    "YouTube": "www.youtube.com",
    "Amazon": "www.amazon.com",
    "Wikipedia": "www.wikipedia.org",
    "Twitter": "www.twitter.com",
    "Instagram": "www.instagram.com",
    "LinkedIn": "www.linkedin.com",
    "Netflix": "www.netflix.com",
    "Reddit": "www.reddit.com",
    "Twitch": "www.twitch.tv",
    "eBay": "www.ebay.com",
    "Pinterest": "www.pinterest.com",
    "Yahoo": "www.yahoo.com",
    "CNN": "www.cnn.com",
    "BBC": "www.bbc.com",
    "The New York Times": "www.nytimes.com",
    "Microsoft": "www.microsoft.com",
    "Apple": "www.apple.com",
    "GitHub": "www.github.com",
    "Stack Overflow": "www.stackoverflow.com",
    "KrebsOnSecurity": "krebsonsecurity.com",
    "The Hacker News": "thehackernews.com",
    "Threatpost": "threatpost.com",
    "Dark Reading": "darkreading.com",
    "Naked Security": "nakedsecurity.sophos.com",
    "Schneier on Security": "schneier.com",
    "Infosec Island": "infosecisland.com",
    "CyberScoop": "cyberscoop.com",
    "SecurityWeek": "securityweek.com",
    "CSO Online": "csoonline.com",
    "SC Magazine": "scmagazine.com",
    "Help Net Security": "helpnetsecurity.com",
    "Cyber Defense Magazine": "cyberdefensemagazine.com",
    "CISO MAG": "cisomag.com",
    "Securelist": "securelist.com",
    "Infosecurity Magazine": "infosecurity-magazine.com",
    "Packet Storm": "packetstormsecurity.com"
}

ip_addresses = {}

for name, url in websites.items():
    try:
        ip_addresses[url] = socket.gethostbyname(url)
    except Exception:
        print('Failed to get address for ' + name)


