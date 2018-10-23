from parameter import para

ReactorPower = para.ReatorPower # T
BoronConcentration = para.BoronConcentration # T
Burnup = para.Burnup # T
InoperableRodNumber = para.InoperableRodNumber # T
InoperableRodName = para.InpoerableRodName # T

def ShutdownMarginCalculation(ReactorPower, Burnup, InoperableRodNumber, InoperableRodName):
    ##################################################
    # BOL일때, 현출력 -> 0% 하기위한 출력 결손량을 계산하자.

    # print(para.HFP)
    # print(para.ReatorPower)
    # print(para.TotalPowerDefect_BOL)

    Equation1 = 'para.HFP:para.TotalPowerDefect_BOL=ReatorPower:x'
    print(Equation1)

    PowerDefect_BOL = para.TotalPowerDefect_BOL * ReactorPower / para.HFP
    print(PowerDefect_BOL)

    ###################################################
    # EOL일때, 현출력 -> 0% 하기위한 출력 결손량을 계산하자.

    #print(para.HFP)
    #print(para.TotalPowerDefect_EOL)
    #print(para.ReatorPower)

    Equation2 = 'para.HFP:para.TotalPowerDefect_EOL=ReactorPower:x'
    print(Equation2)

    PowerDefect_EOL = para.TotalPowerDefect_EOL*ReactorPower/para.HFP
    print(PowerDefect_EOL)

    ####################################################
    # 현재 연소도일때, 현출력 -> 0% 하기위한 출력 결손량을 계산하자.

    #print(para.Burnup_BOL)
    #print(para.Burnup_EOL)
    #print(PowerDefect_BOL)
    #print(PowerDefect_EOL)
    #print(para.Burnup)

    Equation3 = '(para.Burnup_EOL-para.Burnup_BOL):(PowerDefect_EOL-PowerDefect_BOL)=(Burnup-para.Burnup_BOL):(x-PowerDefect_BOL)'
    print(Equation3)

    A = para.Burnup_EOL-para.Burnup_BOL
    #print(A)
    B = PowerDefect_EOL-PowerDefect_BOL
    #print(B)
    C = Burnup-para.Burnup_BOL
    #print(C)

    PowerDefect_Burnup = B*C/A+1602
    print(PowerDefect_Burnup)

    ######################################################
    # 반응도 결손량을 계산하자

    #print(para.VoidCondtent)

    Equation4 = 'PowerDefect_Burnup + para.VoidCondtent'

    PowerDefect_Final=PowerDefect_Burnup + para.VoidCondtent
    print(PowerDefect_Final)

    ######################################################
    # 운전불가능 제어봉 제어능을 계산하자

    #print(para.WorstStuckRodWorth)
    #print(para.InoperableRodNumber)

    Equation4='InoperableRodNumber*para.WorstStuckRodWorth'
    print(Equation4)

    InpoerableRodWorth=InoperableRodNumber*para.WorstStuckRodWorth
    print(InpoerableRodWorth)

    ######################################################
    # 비정상 제어봉 제어능을 계산하자

    #print(para.BankWorth_A)
    #print(para.BankWorth_B)
    #print(para.BankWorth_C)
    #print(para.BankWorth_D)

    Equation5 = 'para.BankWorth_AorBorCorD/8'
    print(Equation5)

    #print(para.InpoerableRodName)

    if InoperableRodName == 'C' :
        #print(para.BankWorth_C)
        AbnormalRodWorth=para.BankWorth_C/8
        print(AbnormalRodWorth)
    elif InoperableRodName == 'A' :
        AbnormalRodWorth = para.BankWorth_A / 8
        print(AbnormalRodWorth)
    elif InoperableRodName == 'B' :
        AbnormalRodWorth = para.BankWorth_B / 8
        print(AbnormalRodWorth)
    elif InoperableRodName == 'D' :
        AbnormalRodWorth = para.BankWorth_D / 8
        print(AbnormalRodWorth)

    #####################################################
    # 운전 불능, 비정상 제어봉 제어능의 합을 계산하자

    #print(InpoerableRodWorth)
    #print(AbnormalRodWorth)

    Equation6 = 'InpoerableRodWorth + AbnormalRodWorth'
    print(Equation6)

    InoperableAbnormal_RodWorth =InpoerableRodWorth + AbnormalRodWorth
    print(InoperableAbnormal_RodWorth)

    #####################################################
    # 현 출력에서의 정지여유도를 계산하자

    #print(para.TotalRodWorth)
    #print(InoperableAbnormal_RodWorth)
    #print(PowerDefect_Final)

    Equation7 = 'para.TotalRodWorth-InoperableAbnormal_RodWorth-PowerDefect_Final'
    print(Equation7)

    ShudownMargin = para.TotalRodWorth-InoperableAbnormal_RodWorth-PowerDefect_Final
    print(ShudownMargin)

    ######################################################
    # 정지여유도 제한치를 만족하는지 비교하자

    #print(para.ShutdownMarginValue)

    if ShudownMargin >= para.ShutdownMarginValue :
        A=print('만족')
    else :
        A=print('불만족')

    return ShudownMargin, A


ShutdownMarginCalculation(ReactorPower=ReactorPower, Burnup=Burnup, InoperableRodNumber=InoperableRodNumber, InoperableRodName=InoperableRodName)