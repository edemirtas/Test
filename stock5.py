import pandas as pd
import numpy as np
import mplfinance as mpf

def main():
    # Örnek veri kullanımı:
    data = {
        'Date': pd.date_range(start='2024-01-01', periods=365),
        'Open': np.random.randint(180, 191, size=365),
        'High': np.random.randint(180, 191, size=365),
        'Low': np.random.randint(180, 191, size=365),
        'Close': np.random.randint(180, 191, size=365),
        'Volume': np.random.randint(1000, 10000, size=365)
    }
    stock_data = pd.DataFrame(data)

    # datetime sütununu index olarak ayarla
    stock_data.set_index('Date', inplace=True)
    stock_data.index = pd.to_datetime(stock_data.index)

    # Mum grafiklerini çiz
    mpf.plot(stock_data, type='candle', volume=True, style='charles')

    # Destek çizgisi ekle
    mpf.plot([stock_data.index[0], stock_data.index[-1]], [150, 150], color='green', linestyle='line')

if __name__ == "__main__":
    main()
