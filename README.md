# 📱 SusDroid

> SusDroid helps you scan Android apps for hidden and suspicious behaviors (like spying or hidden SMS sending) using pattern matching on the app’s internal files.



---

## ✨ Features

- Detects the following suspicious patterns:
  - SMS sending
  - Location access
  - Dynamic code execution
  - WebView URL loading
  - Phone call intents
  - Dangerous permissions in manifest

---

## 🚀 Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Decompile APK (using apktool)

```bash
apktool d target.apk -o target_decompiled
```

### 3. Run analyzer

```bash
python analyzer.py --path target_decompiled --report report.html
```

---

## 📂 Sample Output

```
[*] Scanning for suspicious behavior...

[+] sample_data/AndroidManifest.xml
  ↳ Sensitive Permissions
  ↳ Access Location
  ↳ Send SMS

[+] sample_data/MainActivity.smali
  ↳ Send SMS
  ↳ Access Location
  ↳ Load URL

[✓] Report saved to report.html
```

---

## 📄 License

MIT License
