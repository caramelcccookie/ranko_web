import random as rng

c2=['열기', '어둠', '고통', '전능', '혼', '공명', '생명의 불꽃', '유리구두가', '아마겟돈', '마력', '타천사가', '시험', '교향곡', '영혼', '미궁', '망설임', '흘러나온 한숨', '사모하는 마음', '되살아나는 환영', '그 손', '붉은 입술', '심판', '흔들리는 눈', '감미로운 감옥', '카르마가', '아리아가', '진혼가가', ]
name_person = ['푸른소녀','꽃피는 소녀','세개의 별의 소녀','세기말 가희','방관자','나의 벗이','나의 하인들이','타천사']
name_chu2 = ['성가신 태양이','혼이','공명이','열기가','어둠이','고통이','생명의 불꽃이','교향곡이','마력이','영혼이','망설임이','흘러나온 한숨이','사모하는 마음이', '되살아나는 환영이', '붉은 입술이', '심판이', '흔들리는 눈이', '카르마가', '아리아가', '생명의 불꽃이', '편익의 새들이']

name_place = ['미궁으', '유황불', '몽환의 숲으','황천의 샘으','여기', '인도된 미궁으', '지식의 보고', '몸의 눈물이 흐르는 성전으', '제단으', '피의 궁전으', '아카식 레코드']

verb = ['초대한다', '인도한다', '부른다', '공명한다','내려온다','흘러나온다','춤추며 내려온다']

'''
문장 형식 0 : chu2_name 에 환멸했다냥. 타천사를 시험하려든 미쿠냥 팬 그만두겠냥!
문장 형식 1 : person 이여 place 로 초대하지
문장 형식 2 : c2에 이끌린 person이여, 이 몸에 깃든 c2이(가) 작열한다
문장 형식 3 : person 이여, 신께 받은 이 c2(-조사)! c2으로서 공명하리라
문장 형식 4 : person 이여! 당신도 c2의 소유자인 모양이군
'''

def sentence():
#def sentence(sentence_type):
    sen = '..'
    sentence_type = rng.randrange(0,5)
    if sentence_type == 0:
        sen = rng.choice(name_chu2)[:-1]+'에 환멸했다냥. 타천사를 시험하려든 미쿠냥 팬 그만두겠냥!'
    elif sentence_type == 1:
        tmp1=rng.choice(verb)
        sen=rng.choice(name_person)+'여! '+rng.choice(name_place)+'로 초대하지.'
    elif sentence_type == 2:
        tmp1=rng.choice(c2)
        tmp2=rng.choice(c2)
        while (tmp1==tmp2):
            tmp2=rng.choice(c2)
        if tmp1[-1:]=='가':
            tmp1=tmp1[:-1]
        if tmp2[-1:]!='가':
            tmp2=tmp2+'이'
        sen=tmp1+'에 이끌린 '+rng.choice(name_person)+'여, 이 몸에 깃든 '+tmp2+' '+rng.choice(verb)+'.'
    elif sentence_type == 3:
        tmp1=rng.choice(c2)
        tmp2=rng.choice(c2)
        while (tmp1==tmp2):
            tmp2=rng.choice(c2)
        if tmp1[-1:]=='가':
            tmp1=tmp1[:-1]
        if tmp2[-1:]=='가':
            tmp2=tmp2[:-1]
        sen=rng.choice(name_person)+'여, 신께 받은 이 '+tmp1+'! '+tmp2+'으로서 공명하리라.'
    elif sentence_type == 4:
        tmp1=rng.choice(c2)
        if tmp1[-1:]=='가':
            tmp1=tmp1[:-1]
        sen=rng.choice(name_person)+'여! 당신도 '+tmp1+'의 소유자인 모양이군.'
    return sen
