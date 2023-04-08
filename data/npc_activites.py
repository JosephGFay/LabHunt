import random
activities = {
    'student': {
        'activity': [
            "Taking notes on the lecture",
            "Asking questions when they don't understand something",
            "Participating in group discussions",
            "Texting or messaging their friends",
            "Browsing social media",
            "Daydreaming",
            "Watching videos or movies",
            "Browsing the web for non-class-related topics",
            "Checking their email",
            "Using the restroom",
            "Having a snack",
            "Taking a nap",
            "Listening to music",
            "Reading a book or article",
            "Checking the time",
            "Attending to personal grooming",
            "Chatting with their neighbors",
            "Playing games on their devices",
            "Taking pictures of the lecture slides",
            "Doodling or drawing in their notebook",
            "Zoning out and staring into space",
            "Packing up their belongings early",
            "Checking the weather forecast",
            "Texting their significant other",
            "Making plans for after class",
            "Jotting down reminders for later",
            "Browsing shopping websites",
            "Reading news articles",
            "Researching a topic unrelated to the class",
            "Checking social media notifications",
            "Using their laptop or tablet for non-class-related tasks",
            "Playing with a fidget toy",
            "Watching Tiktoks",
            "Checking their bank account balance",
            "Taking a mental break and closing their eyes",
            "Getting distracted by people-watching",
            "Going on a quick walk outside the classroom",
            "Writing a to-do list for the day",
            "Taking deep breaths to relax",
            "Creating a mental shopping list",
            "Daydreaming about future plans",
            "Browsing job listings online",
            "Reviewing previous lecture notes",
            "Planning their next study session",
            "Checking their social media messages",
            "Texting their family or roommates",
            "Playing clash royale",
        ],

        'screens': [
            'blackboard inside a google chrome browser',
            'a blank windows desktop',
            'a cybersecurity news article about ransomware',
            'a cybersecurity news article about phishing',
            'a news article reporting about a Cryptocurrency heist'
        ],
        'suspicious': [
            # 'does not appear to be doing anything suspicious',
            'does not appear to be doing anything suspicious',


        ],
    },

    'hacker': {
        'screens': [
            'blackboard inside a google chrome browser',
        ],
        'suspicious': [

        ],
    },
}

items = {
    'normal': [

    ],
    'suspicious': [

    ]
}

articles = [
    "Hackers Steal Millions in Cryptocurrency Heist",
    "Cybersecurity Experts Debate the Future of AI in Cyber Defense",
    "Latest Data Breaches and Hacking Incidents",
    "New Phishing Scam Targets Google Drive Users",
    "How to Secure Your Home Network Against Hackers",
    "Ransomware Attack Shuts Down Major US Fuel Pipeline",
    "Cybersecurity Checklist for Small Businesses",
    "FBI Warns of Rise in Online Scams During COVID-19 Pandemic",
    "Cybersecurity Best Practices for Remote Workers",
    "Hackers Exploit Zero-Day Vulnerability in Major Software",
    "Massive Data Breach Affects Millions of Users",
    "Cyberattack on Popular VPN Service Exposes Sensitive User Data",
    "New Malware Campaign Targets Cryptocurrency Investors",
    "Cybercriminals Use Fake Mobile Banking Apps to Steal Login Credentials",
    "Ransomware Attack Hits Major Hospital Network",
    "Phishing Scam Targets Netflix Users with Fake Login Page",
    "Security Researchers Discover New Zero-Day Vulnerability in Widely-Used Software",
    "Outdated Browser Leaves Users Vulnerable to Cyber Attacks",
    "Hackers Steal Credit Card Information from Online Shopping Sites",
    "Cybersecurity Firm Uncovers Massive Data Breach Affecting Millions of Users",
    "Cybersecurity Threats to Watch Out for in 2023",
    "Russian Hackers Target US Government Agencies",
    "Iranian Hackers Target US Defense Contractors",
    "Chinese Hackers Steal Personal Data from Millions of Americans",
    "Cybersecurity Company Accidentally Exposes Customer Data",
    "Cybersecurity Training for Employees: Best Practices",
    "Cybersecurity Risks of IoT Devices in the Workplace",
    "The Importance of Two-Factor Authentication for Online Accounts",
    "Cybersecurity Trends to Watch in 2023",
    "How to Protect Your Small Business from Cyber Threats",
    "Cybersecurity Insurance: Is it Worth the Investment?",
    "Cloud Security: Best Practices for Protecting Your Data",
    "New Malware Variant Targets MacOS Users",
    "Cybersecurity Challenges of Remote Work in the Post-COVID Era",
    "Cybersecurity Risks of Social Media: What You Need to Know",
    "The Cost of Cybercrime: A Look at the Numbers",
    "The Role of Artificial Intelligence in Cybersecurity",
    "Cybersecurity Threats to the Healthcare Industry",
    "The Importance of Regularly Updating Your Software",
    "Cybersecurity Risks of Public Wi-Fi Networks",
    "Cybersecurity Risks of Smart Home Devices",
    "The Pros and Cons of Using a Password Manager",
    "Protecting Your Digital Identity: Best Practices",
    "Cybersecurity Risks of Mobile Devices in the Workplace",
    "Cybersecurity Threats to the Banking Industry",
    "How to Detect and Respond to a Cybersecurity Incident",
    "Cybersecurity Risks of Third-Party Vendors and Contractors",
    "Best Practices for Securing Your Email Account",
    "How to Create a Strong Password: Tips and Tricks",
    "Cybersecurity Challenges of the Internet of Things (IoT)"
]