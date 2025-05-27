import yfinance as yf
import plotly.graph_objects as go

# 글로벌 시총 상위 10개 기업 (사우디 아람코는 제외, 문제 발생 가능)
top_10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "TSMC": "TSM",
    "Eli Lilly": "LLY"
}

# yfinance로 주가 데이터 다운로드
data = yf.download(list(top_10_tickers.values()), period="6mo", group_by='ticker')

# Plotly 그래프 생성
fig = go.Figure()

for company, ticker in top_10_tickers.items():
    try:
        fig.add_trace(go.Scatter(
            x=data[ticker].index,
            y=data[ticker]["Adj Close"],
            mode='lines',
            name=company
        ))
    except KeyError:
        print(f"{ticker}의 데이터를 불러올 수 없습니다.")

# 레이아웃 설정
fig.update_layout(
    title="글로벌 시가총액 상위 10개 기업 주가 (최근 6개월)",
    xaxis_title="날짜",
    yaxis_title="조정 종가 (USD)",
    template="plotly_dark",
    hovermode="x unified"
)

fig.show()
