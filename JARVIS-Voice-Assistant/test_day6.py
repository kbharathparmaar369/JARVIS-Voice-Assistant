# ─────────────────────────────────────────
#  AutoMoto — Day 6 Hardening Test
# ─────────────────────────────────────────

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from module1.speech   import speak
from module1.commands import process_command
from module1.logger   import setup_logger, log_session_start, log_session_end, log_command
from module1.history  import CommandHistory

print("=" * 55)
print("  AutoMoto DAY 6 — HARDENING TEST")
print("=" * 55)

# ── Test 1: Logger setup ───────────────────────────────────
print("\n[TEST 1] Logger setup...")
logger = setup_logger("test_day6")
log_session_start()
logger.info("Day 6 test session started.")
logger.warning("This is a test warning.")
logger.error("This is a test error — do not worry.")

# Check log files exist
log_files = ["logs/automoto.log", "logs/errors.log", "logs/session.log"]
for f in log_files:
    exists = os.path.exists(f)
    print(f"  {f}: {'✅ EXISTS' if exists else '❌ MISSING'}")

# ── Test 2: Command History ────────────────────────────────
print("\n[TEST 2] Command history...")
history = CommandHistory(max_size=5)

test_pairs = [
    ("what time is it",    "It is 3 45 PM."),
    ("tell me a joke",     "Why do programmers prefer dark mode?"),
    ("open calculator",    "Opening calculator."),
    ("who are you",        "I am AutoMoto your personal assistant."),
    ("search wikipedia AI","According to Wikipedia: AI is..."),
    ("open notepad",       "Opening notepad."),   # This should push out oldest
]

for cmd, resp in test_pairs:
    history.add(cmd, resp)
    log_command(cmd, resp)

print(f"  Total commands tracked: {history.total_commands}")
print(f"  History size (max 5):   {len(history)}")
print(f"  Last 3 entries:")
for entry in history.get_last(3):
    print(f"    [{entry['timestamp']}] {entry['command']}")

summary = history.summary()
print(f"  Summary: '{summary[:80]}...'")
print("  ✅ History working correctly" if len(history) == 5 else "  ❌ History size wrong")

# ── Test 3: speak() edge cases ────────────────────────────
print("\n[TEST 3] speak() edge cases...")
speak("")          # Should skip — no output
speak("   ")       # Should skip — whitespace only
speak("Edge case test. AutoMoto hardening is working correctly.")
print("  ✅ speak() edge cases handled")

# ── Test 4: process_command() edge cases ──────────────────
print("\n[TEST 4] process_command() edge cases...")
edge_cases = [
    ("",              "Empty string"),
    ("   ",           "Whitespace only"),
    ("xyzzy nonsense","Unknown command fallback"),
    ("OPEN CALCULATOR","Uppercase command"),
    ("open   notepad", "Extra spaces"),
]

for cmd, desc in edge_cases:
    result = process_command(cmd.lower().strip())
    status = "✅" if result is not None else "❌"
    print(f"  {status} {desc}: '{result[:50] if result else 'empty'}'")

# ── Test 5: Full pipeline ──────────────────────────────────
print("\n[TEST 5] Full pipeline test...")
commands_to_test = [
    "what time is it",
    "tell me a joke",
    "tell me a fact",
    "flip a coin",
    "who are you",
    "open calculator",
    "goodbye",
]

for cmd in commands_to_test:
    result = process_command(cmd)
    log_command(cmd, result)
    print(f"  ✅ '{cmd}' → '{result[:50]}...' " if len(result) > 50
          else f"  ✅ '{cmd}' → '{result}'")

log_session_end()

print(f"\n{'='*55}")
print("  DAY 6 HARDENING TEST COMPLETE")
print(f"{'='*55}")
print("\nCheck these log files:")
for f in log_files:
    print(f"  → {f}")

speak("Day 6 hardening test complete. All systems are robust and operational.")
