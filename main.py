import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Örnek Telekom Müşteri Veri Seti
veri = {
    'Kullanim_Suresi_Ay': [2, 24, 1, 12, 36, 5, 48, 3, 60, 8],
    'Aylik_Fatura_TL': [120, 70, 150, 90, 60, 110, 50, 130, 45, 100],
    'Destek_Talebi_Sayisi': [5, 1, 4, 2, 0, 3, 1, 6, 0, 4],
    'Terk_Etti_Mi': [1, 0, 1, 0, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(veri)

# 2. Girdi (X) ve Çıktı (y) Değişkenleri
X = df[['Kullanim_Suresi_Ay', 'Aylik_Fatura_TL', 'Destek_Talebi_Sayisi']]
y = df['Terk_Etti_Mi']

# 3. Train / Test Bölünmesi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Karar Ağacı Model Eğitimi
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Tahmin ve Başarı Ölçümü
tahminler = model.predict(X_test)
dogruluk = accuracy_score(y_test, tahminler)

print("=== CHURN TAHMİN MODELİ SONUÇLARI ===")
print(f"Model Doğruluk Oranı (Accuracy): %{dogruluk * 100:.0f}\n")

# 6. Yeni Müşteri Tahmini
yeni_musteri = [[4, 140, 5]]
tahmin = model.predict(yeni_musteri)

if tahmin[0] == 1:
    print("⚠️ UYARI: Bu müşterinin şirketi TERK ETME riski yüksek! (Aksiyon alınmalı)")
else:
    print("✅ Bu müşteri hizmet almaya devam edecek görünüyor.")
