"""
═══════════════════════════════════════════════════════════════
  TRADING BOT - SYSTÈME COMPLET
  Toutes les 18 compétences intégrées
  Auteur : Gates / Alinyxe
═══════════════════════════════════════════════════════════════
"""

import time
import logging
import signal
import sys
from datetime import datetime

from core.bot_engine import BotEngine
from core.config import Config
from reporting.logger import setup_logger
from reporting.reporter import Reporter

# ─────────────────────────────────────────
# DÉMARRAGE
# ─────────────────────────────────────────
def main():
    setup_logger()
    log = logging.getLogger("MAIN")
    log.info("═" * 55)
    log.info("  TRADING BOT DÉMARRÉ — " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    log.info("═" * 55)

    config = Config()
    bot = BotEngine(config)

    # Arrêt propre avec CTRL+C
    def shutdown(sig, frame):
        log.warning("⚠️  Signal d'arrêt reçu — fermeture propre...")
        bot.emergency_stop("Arrêt manuel")
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    # Backtesting avant démarrage réel
    if config.RUN_BACKTEST_FIRST:
        log.info("📊 Backtesting en cours...")
        bot.run_backtest()

    # Paper trading ou réel
    if config.PAPER_TRADING:
        log.info("🧪 MODE PAPER TRADING activé (argent fictif)")
    else:
        log.warning("💰 MODE RÉEL ACTIVÉ — Argent réel engagé !")

    bot.run()


if __name__ == "__main__":
    main()
