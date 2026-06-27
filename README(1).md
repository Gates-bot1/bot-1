# ⚡ TRADING BOT — Documentation complète

## Structure du projet

```
tradingbot/
├── main.py                    # Point d'entrée
├── requirements.txt
├── .env.example               # → renommer en .env
│
├── core/
│   ├── config.py              # Tous les paramètres
│   └── bot_engine.py          # Moteur principal
│
├── data/
│   ├── market_data.py         # Connexion Binance + données temps réel
│   └── sentiment.py           # Fear&Greed, news, CoinGecko
│
├── strategy/
│   ├── indicators.py          # RSI, MACD, BB, EMA, ATR, S/R...
│   ├── signal_engine.py       # Génération de signaux
│   ├── regime_detector.py     # Bull / Bear / Sideways
│   └── backtester.py          # Backtest + optimisation auto
│
├── risk/
│   ├── risk_manager.py        # Probabilité, espérance, taille position
│   └── portfolio_manager.py   # Gestion multi-paires, capital
│
├── execution/
│   └── executor.py            # Ordres Binance (paper + réel)
│
├── ml/
│   └── learning_engine.py     # Apprentissage, détection erreurs
│
└── reporting/
    ├── reporter.py            # Rapports + Telegram
    └── logger.py              # Logs
```

## 18 compétences intégrées

| # | Compétence | Fichier |
|---|-----------|---------|
| 1 | Analyse marché temps réel | market_data.py |
| 2 | Analyse technique avancée | indicators.py |
| 3 | Prise de décision autonome | signal_engine.py + bot_engine.py |
| 4 | Calcul probabilité / risque | risk_manager.py |
| 5 | Gestion du risque intelligente | risk_manager.py |
| 6 | Apprentissage continu (ML) | learning_engine.py |
| 7 | Adaptation au marché | regime_detector.py + signal_engine.py |
| 8 | Sources de données externes | market_data.py + sentiment.py |
| 9 | Analyse de sentiment | sentiment.py |
| 10 | Backtesting | backtester.py |
| 11 | Paper Trading / Simulation | executor.py |
| 12 | Détection d'erreurs | learning_engine.py |
| 13 | Optimisation automatique | backtester.py |
| 14 | Exécution rapide | executor.py |
| 15 | Gestion du portefeuille | portfolio_manager.py |
| 16 | Reporting / Assistant business | reporter.py |
| 17 | Système d'urgence | bot_engine.py + reporter.py |
| 18 | Vision long terme (évolution) | learning_engine.py |

## Installation

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Configurer les clés API
cp .env.example .env
# Édite .env avec tes clés

# 3. Configurer le bot
# Ouvre core/config.py et ajuste selon tes besoins

# 4. Lancer en paper trading (PAPER_TRADING = True dans config.py)
python main.py
```

## Configuration essentielle (core/config.py)

```python
PAPER_TRADING = True        # False = argent réel
INITIAL_CAPITAL = 1000.0    # Capital de départ
SYMBOLS = ["BTC/USDT", ...]  # Paires à trader
MIN_CONFIDENCE = 65         # Signal minimum accepté
MAX_RISK_PER_TRADE = 0.02   # 2% max par trade
```

## Avertissement

Ce bot est un outil d'aide à la décision.
Aucun système de trading ne garantit des profits.
Commence TOUJOURS en paper trading avant le mode réel.
