from crewai import Agent
from crewai.tools import BaseTool
import pandas as pd
from typing import Dict, Any

class LoadFinancialDataTool(BaseTool):
    name: str = "load_financial_data"
    description: str = "BS, PL, MSC 파일 경로를 받아 표준화된 DataFrame dict로 반환"

    def _run(
        self,
        bs_path: str,
        pl_path: str,
        msc_path: str
    ) -> Dict[str, Any]:
        print(f"[INFO] BS 파일 경로: {bs_path}")
        print(f"[INFO] PL 파일 경로: {pl_path}")
        print(f"[INFO] MSC 파일 경로: {msc_path}")

        # pandas로 엑셀 파일 읽기
        df_bs  = pd.read_excel(bs_path, sheet_name=0, header=0)
        df_pl  = pd.read_excel(pl_path, sheet_name=0, header=0)
        df_msc = pd.read_excel(msc_path, sheet_name=0, header=0)

        # 기본 전처리: 첫 열을 인덱스로, 빈 행/열 제거
        for df in (df_bs, df_pl, df_msc):
            df.set_index(df.columns[0], inplace=True)
            df.dropna(axis=0, how="all", inplace=True)
            df.dropna(axis=1, how="all", inplace=True)

        return {
            "balance_sheet": df_bs,
            "income_statement": df_pl,
            "cost_sheet": df_msc,
        }

load_data_tool = LoadFinancialDataTool()

data_loader_agent = Agent(
    role="재무제표 정제 담당자",
    goal="BS, PL, MSC 파일을 pandas DataFrame으로 변환",
    backstory="각 파일 경로를 받아 자동으로 DataFrame을 만들어 주는 전문가",
    tools=[load_data_tool],
    verbose=True,
)

