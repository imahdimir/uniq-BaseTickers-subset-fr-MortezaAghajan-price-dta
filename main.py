##

from dataclasses import dataclass

from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import read_data_according_to_type as rdata
from mirutil.funcs import save_df_as_a_nice_xl as sxl
from mirutil.funcs import save_as_prq_wo_index as sprq



btic = 'BaseTicker'
isbtic = 'IsBT'

@dataclass
class Cols :
  name = 'name'
  gn = 'group_name'
  market = 'market'
  title = 'title'

cols = Cols()


def main() :

  pass

  ##

  # df = rdata('pr.prq')
  # ##
  # for cn in df.columns :
  #   print('"' + cn + '":None,')
  # ##
  # cols2keep = {
  #     "group_name" : None ,
  #     "name"       : None ,
  #     "title"      : None ,
  #     "market"     : None ,
  #     }
  #
  # df = df[cols2keep.keys()]
  # df = df.drop_duplicates()
  # ##
  # df = df.applymap(norm)
  # df = df.drop_duplicates()
  # ##
  # sprq(df, 'in.prq')

  ##


  df = rdata('dta/in.prq')
  ##
  not_bt = {
      'بازار ابزارهای مشتقه'             : None ,
      'بازار ابزارهای مشتقه فرابورس'     : None ,
      'بازار ابزارهای نوین مالی فرابورس' : None ,
      'بازار اوراق بدهی'                 : None ,
      'بازار جبرانی بورس'                : None ,
      'بازار خرده فروشی بورس'            : None ,
      'بازار معاملات عمده بورس'          : None ,
      'بازار عادی آتی'                   : None ,
      'بورس کالا'                        : None ,
      'بورس انرژی'                       : None ,
      }

  msk = df['market'].isin(not_bt.keys())
  df.loc[msk , isbtic] = False

  msk = df[isbtic].ne(False)
  df3 = df[msk]
  ##
  ptr0 = r'ح' + r'\s?\.' + r'.+'
  msk = df[cols.title].str.fullmatch(ptr0)

  ptr0_1 = r'ح' + r'\s.+'
  msk |= df[cols.title].str.fullmatch(ptr0_1)

  df.loc[msk, isbtic] = False

  msk = df[isbtic].ne(False)
  df1 = df[msk]
  ##
  df1 = df1[cols.name].to_frame()
  df1 = df1.drop_duplicates()
  df1 = df1.rename(columns = {
      cols.name : btic
      })
  ##
  sxl(df1 , 'dta/Unique-BaseTickers-TSETMC.xlsx')

##


if __name__ == "__main__" :
  main()