while True:
    try:
        hi,mi,ha,ma=map(int, input().split())
        if hi!=0 or mi!=0 or ha!=0 or ma!=0:
            if ha>=hi and ma >= mi:
                hf=ha-hi
                mf=ma-mi
                me=hf*60
                minutos=mf+me
            elif ha>hi and ma<mi:
                hf=ha-hi
                mf=ma-(mi-60)
                he=hf-1
                me=he*60
                minutos=mf+me
            elif ha<hi and ma>=mi:
                hf=ha-(hi-24)
                mf=ma-mi
                me=hf*60
                minutos=mf+me
            elif ha<=hi and ma<mi:
                hf=ha-(hi-24)
                mf=ma-(mi-60)
                he=hf-1
                me=he*60
                minutos=mf+me
            print(minutos)
        else:
            break
    except EOFError:
        break
