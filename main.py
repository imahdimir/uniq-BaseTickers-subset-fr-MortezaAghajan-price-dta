##

from dataclasses import dataclass

from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import read_data_according_to_type as rdata
from mirutil.funcs import save_df_as_a_nice_xl as sxl


man_btic_name = {  # those with number in their base tickers
    'آتی1' : None ,
    'بورس1' : None ,
    'بورس2' : None ,
    'بورس3' : None ,
    }

khord_2 = 'بازار خرده فروشی بورس'
jobrani_3 = 'بازار جبرانی بورس'
omde_4 = 'بازار معاملات عمده بورس'
btic = 'BaseTicker'

@dataclass
class Cols :
  name = 'name'
  gn = 'group_name'
  market = 'market'
  title = 'title'

cols = Cols()

@dataclass
class GroupNames :
  oragh = "اوراق تامین مالی"
  oragh_maskan = 'اوراق حق تقدم استفاده از تسهیلات مسکن'
  oragh_ip = 'اوراق بهادار مبتنی بر دارایی فکری'

gpns = GroupNames()

def main() :

  pass

  ##


  df = rdata('in.prq')
  ##
  for cn in df.columns :
    print('"' + cn + '":None,')
  ##
  cols2keep = {
      "group_name" : None ,
      "name"       : None ,
      "title"      : None ,
      "market"     : None ,
      }

  df = df[cols2keep.keys()]
  df = df.drop_duplicates()
  ##
  df = df.applymap(norm)
  ##
  ptr = '\D+'
  msk = df[cols.name].str.fullmatch(ptr)

  msk &= ~ df[cols.market].isin([khord_2 , jobrani_3 , omde_4])

  ptr0 = r'ح' + r'\s?\.' + r'.+'
  msk &= ~ df[cols.title].str.fullmatch(ptr0)

  ptr0_1 = r'ح' + r'\s.+'
  msk &= ~ df[cols.title].str.fullmatch(ptr0_1)

  ptr1 = r'اختیارخ' + r'\s.+'
  msk &= ~ df[cols.title].str.fullmatch(ptr1)

  ptr2 = r'اختیارف' + r'\s.+'
  msk &= ~ df[cols.title].str.fullmatch(ptr2)

  ptr3 = r'آتی' + r'\s.+'
  msk &= ~ df[cols.title].str.fullmatch(ptr3)

  ptr4 = r'صکوک' + r'\s.+'
  msk &= ~ df[cols.title].str.fullmatch(ptr4)

  msk &= ~ df[cols.gn].isin([gpns.oragh , gpns.oragh_maskan , gpns.oragh_ip])

  msk |= df[cols.name].isin(man_btic_name.keys())

  df1 = df[msk]
  ##
  df1 = df1[cols.name].to_frame()
  df1 = df1.drop_duplicates()
  df1 = df1.rename(columns = {
      cols.name : btic
      })
  ##
  sxl(df1 , 'Unique-BaseTickers-TSETMC.xlsx')

##


if __name__ == "__main__" :
  main()