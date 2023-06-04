def hamtimsodiem(mangdiemhocsinh, diemcantim):
    sodiem = 0
    for diem in mangdiemhocsinh:
        if diem == diemcantim :
            sodiem = sodiem + 1
    print ("so diem bang %s la %s" % (diemcantim,sodiem))
    return 

def hamtinhchuvihinhchunhat(cd,cr):
    chuvihinhchunhat = (cd + cr) * 2 #12
    return chuvihinhchunhat

def hamtinhdientichhinhvuong(chieudaicanh):
    if chieudaicanh==0 :
        print("chieu dai canh gi ma bang khong ong noi")
        return "dien tich khong tinh duoc"

    dientichhinhvuong = chieudaicanh * chieudaicanh
    return dientichhinhvuong