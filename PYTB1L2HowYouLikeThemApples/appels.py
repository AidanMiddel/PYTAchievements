bomen = int("333") #aantel bomen
schaduw_procent = float(2 / 3) #percentage van de bomen die in de schaduw staat
schaduw_appels_procent = float("0.8") #hoeveel procent van de appels een schaduw boom levert
zon_procent = float(1 / 3) #percentage van de bomen die in de zon staat
appels_pb_zon = int("146") #hoeveel appels per boom die in de zon staat er af komt
appels_pb_schaduw = appels_pb_zon * schaduw_appels_procent; # de 80% die schaduw bomen leveren

bomen_in_schaduw = bomen * schaduw_procent; #hoeveel bomen in de schaduw staan
bomen_in_zon = bomen * zon_procent; #hoeveel bomen in de zon staan

alle_appels_shaduw = bomen_in_schaduw * appels_pb_schaduw;
alle_appels_zon = bomen_in_zon * appels_pb_zon;
alle_appels = alle_appels_shaduw + alle_appels_zon;
appels_pp = alle_appels / int(3);
appels_pp_geenkomma = appels_pp - float("0.200000000003")

print("appels per persoon: ", appels_pp_geenkomma)
