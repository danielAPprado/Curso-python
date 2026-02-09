metro = float(input('Digite quantos metros pretende converter '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print('A quantidade de metros {} pode ser convertida em \n {:.2f} km. \n {:.2f} hm. \n {:.2f} dam. \n {:.2f} dm. \n {:.2f} cm. \n {:.2f} mm.'.format(metro, km, hm, dam, dm, cm, mm))
