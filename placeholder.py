import time, os, datetime
print("✅ MentorBot placeholder container запущен. Ждём код от Codex…")
print("ENV check: TELEGRAM_TOKEN set =", bool(os.environ.get("TELEGRAM_TOKEN")))
while True:
    print("⏳ alive", datetime.datetime.utcnow().isoformat()+"Z")
    time.sleep(30)
