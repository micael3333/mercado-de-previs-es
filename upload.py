import os
from github import Github # Requer: pip install PyGithub

# ==========================================
# ⚙️ CONFIGURAÇÕES
# ==========================================
# SEU TOKEN (O mesmo que já usamos)
GITHUB_TOKEN = "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"

# SEU REPOSITÓRIO
REPO_NAME = "micael3333/Fx-hedge" 
BRANCH = "main"

# DADOS DO AFILIADO
LINK_AFILIADO = "https://one.exnessonelink.com/a/s5gxvteezq"
EMAIL_CONTATO = "micaelvasques344@gmail.com"
CPF_CONTATO = "053.225.641-79"
ENDERECO_FISICO = "1 Sandton Dr, Sandhurst, Sandton, 2196, South Africa (Partner Office)"
NOME_SITE = "PrimeFluxo"

# ==========================================
# 0. CONFIGURAÇÃO VERCEL (Clean URLs)
# ==========================================
vercel_json = """
{
  "cleanUrls": true,
  "trailingSlash": false
}
"""

# ==========================================
# 1. ESTÉTICA (CSS)
# ==========================================
css_content = """
:root { --primary: #0a2540; --accent: #00d084; --text: #333; --bg-light: #f8f9fa; --white: #fff; --font-head: 'Montserrat', sans-serif; --font-body: 'Roboto', sans-serif; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font-body); color: var(--text); line-height: 1.6; background: var(--bg-light); }
a { text-decoration: none; transition: 0.3s; }
header { background: var(--white); box-shadow: 0 2px 15px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 1000; }
.nav-container { max-width: 1100px; margin: 0 auto; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
.logo { font-family: var(--font-head); font-weight: 800; font-size: 1.5rem; color: var(--primary); letter-spacing: -1px; }
.menu a { margin-left: 25px; color: var(--primary); font-weight: 500; font-size: 0.95rem; }
.menu a:hover { color: var(--accent); }
.btn-nav { background: var(--accent); color: var(--white) !important; padding: 10px 25px; border-radius: 4px; font-weight: 700; }
.btn-nav:hover { background: #00b070; transform: translateY(-1px); }
.hero { background: linear-gradient(135deg, #0a2540 0%, #163252 100%); color: var(--white); padding: 100px 20px; text-align: center; }
.hero h1 { font-family: var(--font-head); font-size: 2.8rem; margin-bottom: 20px; line-height: 1.1; }
.hero p { max-width: 700px; margin: 0 auto 35px; font-size: 1.2rem; opacity: 0.9; }
.btn-hero { background: var(--accent); color: var(--white); padding: 15px 40px; border-radius: 5px; font-weight: 700; font-size: 1rem; display: inline-block; }
.section { padding: 80px 20px; max-width: 1100px; margin: 0 auto; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 40px; }
.card { background: var(--white); padding: 35px; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-top: 4px solid var(--accent); transition: transform 0.3s; }
.card:hover { transform: translateY(-5px); }
.card h3 { color: var(--primary); margin-bottom: 15px; font-family: var(--font-head); }
.table-container { overflow-x: auto; margin-top: 30px; background: var(--white); border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
table { width: 100%; border-collapse: collapse; min-width: 600px; }
th { background: var(--primary); color: var(--white); padding: 18px; text-align: left; }
td { padding: 18px; border-bottom: 1px solid #eee; color: #555; }
tr:last-child td { border-bottom: none; }
footer { background: #051525; color: #8898aa; padding: 60px 20px 20px; font-size: 0.9rem; }
.footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; max-width: 1100px; margin: 0 auto; }
.footer-links a { display: block; color: #ccc; margin-bottom: 8px; }
.risk-box { margin-top: 50px; padding: 20px; border-top: 1px solid #333; text-align: center; font-size: 0.8rem; background: #0a0a0a; color: #ff6b6b; }
"""

# ==========================================
# 2. PÁGINA HOME (index.html)
# ==========================================
index_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{NOME_SITE} | Institutional STP & Hedging Solutions</title>
    <meta name="description" content="Discover true STP execution brokers in South Africa. Full hedging allowed, raw spreads from 0.0 pips.">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="nav-container">
            <div class="logo">{NOME_SITE}.</div>
            <div class="menu">
                <a href="/">Home</a>
                <a href="/review">Broker Review</a>
                <a href="/terms">Terms</a>
                <a href="{LINK_AFILIADO}" target="_blank" class="btn-nav">Open Raw Account</a>
            </div>
        </div>
    </header>

    <div class="hero">
        <h1>Institutional-Grade STP Execution<br>for South African Traders.</h1>
        <p>Unrestricted Environment: Full Hedging Capabilities, Raw Spreads (0.0 pips), and Instant Crypto/USDT Withdrawals.</p>
        <a href="/review" class="btn-hero">Analyze Top STP Broker</a>
    </div>

    <div class="section">
        <div class="grid">
            <div class="card">
                <h3>🛡️ Full Hedging Freedom</h3>
                <p>Bypass FIFO restrictions. Open Long and Short positions simultaneously. Ideal for complex arbitrage.</p>
            </div>
            <div class="card">
                <h3>⚡ True STP Execution</h3>
                <p>Direct Market Access (DMA) with no dealing desk intervention. Orders matched at liquidity speeds under 25ms.</p>
            </div>
            <div class="card">
                <h3>🤖 Algo & Scalping Ready</h3>
                <p>Optimized infrastructure for MT4/MT5 EAs. Zero slippage on major pairs during volatility.</p>
            </div>
        </div>
    </div>

    <footer>
        <div class="footer-grid">
            <div>
                <h4 style="color:#fff; margin-bottom:15px;">{NOME_SITE}</h4>
                <p>Independent Financial Marketing Partner.</p>
                <p>{ENDERECO_FISICO}</p>
            </div>
            <div class="footer-links">
                <h4 style="color:#fff; margin-bottom:15px;">Company</h4>
                <a href="/terms">Terms & Conditions</a>
                <a href="/privacy">Privacy Policy</a>
                <a href="/compliance">Risk Disclosure</a>
            </div>
            <div class="footer-links">
                <h4 style="color:#fff; margin-bottom:15px;">Contact</h4>
                <a href="mailto:{EMAIL_CONTATO}">Email Us</a>
                <span style="color:#ccc; font-size:0.8rem">ID: {CPF_CONTATO}</span>
            </div>
        </div>
        <div class="risk-box">
            <strong>RISK WARNING:</strong> CFDs are complex instruments. 
            <strong>78.3% of retail investor accounts lose money when trading CFDs with this provider.</strong> 
        </div>
    </footer>
</body>
</html>
"""

# ==========================================
# 3. PÁGINA REVIEW (review.html)
# ==========================================
review_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exness Review 2025 | STP & Raw Spread Analysis</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="nav-container">
            <div class="logo">{NOME_SITE}.</div>
            <div class="menu">
                <a href="/">Home</a>
                <a href="/review">Broker Review</a>
                <a href="{LINK_AFILIADO}" target="_blank" class="btn-nav">Open Account</a>
            </div>
        </div>
    </header>

    <div class="section">
        <h1>Exness Technical Review: The Ultimate STP Solution?</h1>
        <p>For professional traders in South Africa searching for <strong>"brokers STP"</strong> or effective <strong>"hedging forex"</strong> strategies.</p>
        
        <div class="table-container">
            <table>
                <thead>
                    <tr><th>Feature</th><th>Standard Market Maker</th><th>Exness (Raw Spread)</th></tr>
                </thead>
                <tbody>
                    <tr><td><strong>Spread (EURUSD)</strong></td><td>1.2 pips</td><td><strong>0.0 pips</strong></td></tr>
                    <tr><td><strong>Execution Model</strong></td><td>Dealing Desk</td><td><strong>STP / NDD</strong></td></tr>
                    <tr><td><strong>Hedging Policy</strong></td><td>Restricted</td><td><strong>Allowed</strong></td></tr>
                    <tr><td><strong>Withdrawals</strong></td><td>1-3 Days</td><td><strong>Instant</strong></td></tr>
                </tbody>
            </table>
        </div>
        <br>
        <div class="grid">
            <div class="card">
                <h3>1. Raw Spread Dynamics</h3>
                <p>Unlike standard accounts, the Raw Spread account offers spreads from 0.0 pips with a fixed commission. Critical for scalping and EAs.</p>
            </div>
            <div class="card">
                <h3>2. Instant Withdrawals</h3>
                <p>Exness processes withdrawals instantly via local SA banks and USDT. High capital efficiency.</p>
            </div>
        </div>
        <br><br>
        <center>
            <a href="{LINK_AFILIADO}" target="_blank" class="btn-hero">Open Raw Spread Account</a>
        </center>
    </div>

    <footer>
        <div class="footer-grid">
            <div>
                <h4 style="color:#fff; margin-bottom:15px;">Legal</h4>
                <a href="/terms">Terms of Use</a>
                <a href="/privacy">Privacy Policy</a>
            </div>
        </div>
        <div class="risk-box">
            <strong>78.3% of retail accounts lose money.</strong> Use leverage responsibly.
        </div>
    </footer>
</body>
</html>
"""

# ==========================================
# 4. PÁGINA COMPLIANCE/RISK (compliance.html)
# ==========================================
compliance_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Risk Disclosure | {NOME_SITE}</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="nav-container">
            <div class="logo">{NOME_SITE}.</div>
            <div class="menu">
                <a href="/">Home</a>
                <a href="/review">Review</a>
            </div>
        </div>
    </header>

    <div class="section">
        <h1>Risk Disclosure & Advertiser Policy</h1>
        
        <div class="card">
            <h3>Advertiser Disclosure</h3>
            <p>{NOME_SITE} is an independent comparison website funded by referral fees. We are not a financial service provider.</p>

            <h3 style="margin-top:30px;">High Risk Warning</h3>
            <p>Trading Forex and CFDs involves a high level of risk to your capital. <strong>78% to 89% of retail investor accounts lose money.</strong></p>

            <h3 style="margin-top:30px;">Contact</h3>
            <p><strong>Representative:</strong> Micael Vasques</p>
            <p><strong>Tax ID:</strong> {CPF_CONTATO}</p>
            <p><strong>Email:</strong> {EMAIL_CONTATO}</p>
        </div>
    </div>
    
    <footer>
        <div class="risk-box">Risk Warning: 78.3% of retail investor accounts lose money.</div>
    </footer>
</body>
</html>
"""

# ==========================================
# 5. NOVA PÁGINA: TERMS (terms.html)
# ==========================================
terms_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms & Conditions | {NOME_SITE}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="nav-container">
            <div class="logo">{NOME_SITE}.</div>
            <div class="menu"><a href="/">Home</a></div>
        </div>
    </header>
    <div class="section">
        <h1>Terms and Conditions</h1>
        <div class="card">
            <p><strong>Last Updated: November 2025</strong></p>
            <br>
            <h3>1. Introduction</h3>
            <p>Welcome to {NOME_SITE}. By accessing this website, you agree to be bound by these Terms and Conditions.</p>
            <br>
            <h3>2. No Financial Advice</h3>
            <p>The content on this site is for informational purposes only. It does not constitute financial advice. We do not provide investment recommendations.</p>
            <br>
            <h3>3. Third-Party Links</h3>
            <p>Our site contains links to third-party websites (such as brokers). We are not responsible for the content or privacy practices of these sites.</p>
            <br>
            <h3>4. Limitation of Liability</h3>
            <p>{NOME_SITE} and its owners shall not be held liable for any loss or damage resulting from the use of this information.</p>
        </div>
    </div>
    <footer><div class="risk-box">Use leverage responsibly.</div></footer>
</body>
</html>
"""

# ==========================================
# 6. NOVA PÁGINA: PRIVACY (privacy.html)
# ==========================================
privacy_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy | {NOME_SITE}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="nav-container">
            <div class="logo">{NOME_SITE}.</div>
            <div class="menu"><a href="/">Home</a></div>
        </div>
    </header>
    <div class="section">
        <h1>Privacy Policy</h1>
        <div class="card">
            <p><strong>Effective Date: November 2025</strong></p>
            <br>
            <h3>1. Data Collection</h3>
            <p>We do not collect personal data such as names or emails directly, unless you contact us via email. We may use cookies for site analytics.</p>
            <br>
            <h3>2. Cookies</h3>
            <p>We use third-party cookies to analyze traffic and improve user experience. By using this site, you consent to the use of cookies.</p>
            <br>
            <h3>3. Affiliate Disclosure</h3>
            <p>We participate in affiliate marketing programs. Clicking on links may result in a commission credited to us, at no extra cost to you.</p>
        </div>
    </div>
    <footer><div class="risk-box">Use leverage responsibly.</div></footer>
</body>
</html>
"""

# ==========================================
# 7. EXECUÇÃO DO UPLOAD
# ==========================================
def deploy_site():
    print(f"🚀 Iniciando Deploy para: {REPO_NAME}")
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        print(f"✅ Repositório conectado!")
    except Exception as e:
        print(f"❌ ERRO: {e}")
        return

    files = {
        "vercel.json": vercel_json,
        "styles.css": css_content,
        "index.html": index_html,
        "review.html": review_html,
        "compliance.html": compliance_html,
        "terms.html": terms_html,       # <--- Novo arquivo
        "privacy.html": privacy_html    # <--- Novo arquivo
    }

    for filename, content in files.items():
        try:
            contents = repo.get_contents(filename, ref=BRANCH)
            repo.update_file(contents.path, f"Update {filename}", content, contents.sha, branch=BRANCH)
            print(f"🔄 Atualizado: {filename}")
        except:
            repo.create_file(filename, f"Create {filename}", content, branch=BRANCH)
            print(f"✨ Criado: {filename}")

    print("\n✅ SITE 3.0 NO AR! Termos e Privacidade adicionados.")

if __name__ == "__main__":
    deploy_site()