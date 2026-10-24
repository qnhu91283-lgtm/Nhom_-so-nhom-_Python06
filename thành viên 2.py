
class SinhVien:
    def __init__(self, ma_sv, ho_ten, lop, gpa, diem_rl):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.lop = lop
        self.gpa = float(gpa)
        self.diem_rl = int(diem_rl)


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def tim_theo_ma(self, ma_sv):
        for sv in self.danh_sach:
            if sv.ma_sv.lower() == ma_sv.strip().lower():
                return sv
        return None

    def them_sinh_vien(self, sv):
        if self.tim_theo_ma(sv.ma_sv):
            print("Ma sinh vien da ton tai!")
            return False

        self.danh_sach.append(sv)
        print("Them thanh cong!")
        return True

    def sua_sinh_vien(self, ma_sv):
        sv = self.tim_theo_ma(ma_sv)

        if sv is None:
            print("Khong tim thay sinh vien!")
            return

        ho_ten = input("Nhap ho ten moi: ").strip()
        lop = input("Nhap lop moi: ").strip()

        try:
            gpa = float(input("Nhap GPA moi (0-4): "))
            diem_rl = int(input("Nhap diem ren luyen moi (0-100): "))

            if not 0 <= gpa <= 4 or not 0 <= diem_rl <= 100:
                print("Diem khong hop le!")
                return

        except ValueError:
            print("Vui long nhap dung kieu du lieu!")
            return

        if ho_ten:
            sv.ho_ten = ho_ten
        if lop:
            sv.lop = lop

        sv.gpa = gpa
        sv.diem_rl = diem_rl
        print("Sua thanh cong!")

    def xoa_sinh_vien(self, ma_sv):
        sv = self.tim_theo_ma(ma_sv)

        if sv is None:
            print("Khong tim thay sinh vien!")
            return

        self.danh_sach.remove(sv)
        print("Xoa thanh cong!")

    def tim_kiem(self, tu_khoa):
        tu_khoa = tu_khoa.lower().strip()

        ket_qua = []
        for sv in self.danh_sach:
            if (tu_khoa in sv.ma_sv.lower()
                    or tu_khoa in sv.ho_ten.lower()
                    or tu_khoa in sv.lop.lower()):
                ket_qua.append(sv)

        self.hien_thi(ket_qua)

    def hien_thi(self, ds=None):
        if ds is None:
            ds = self.danh_sach

        if not ds:
            print("Danh sach sinh vien trong!")
            return

        print("-" * 70)
        print(f"{'Ma SV':<12}{'Ho ten':<22}{'Lop':<12}{'GPA':<8}{'Diem RL'}")
        print("-" * 70)

        for sv in ds:
            print(
                f"{sv.ma_sv:<12}{sv.ho_ten:<22}"
                f"{sv.lop:<12}{sv.gpa:<8.2f}{sv.diem_rl}"
            )

        print("-" * 70)


def them_sinh_vien(ql):
    ma_sv = input("Nhap ma sinh vien: ").strip()

    if not ma_sv:
        print("Ma sinh vien khong duoc de trong!")
        return

    if ql.tim_theo_ma(ma_sv):
        print("Ma sinh vien da ton tai!")
        return

    ho_ten = input("Nhap ho ten: ").strip()
    lop = input("Nhap lop: ").strip()

    if not ho_ten or not lop:
        print("Ho ten va lop khong duoc de trong!")
        return

    try:
        gpa = float(input("Nhap GPA (0-4): "))
        diem_rl = int(input("Nhap diem ren luyen (0-100): "))

        if not 0 <= gpa <= 4:
            print("GPA phai tu 0 den 4!")
            return

        if not 0 <= diem_rl <= 100:
            print("Diem ren luyen phai tu 0 den 100!")
            return

    except ValueError:
        print("Du lieu diem khong hop le!")
        return

    sv = SinhVien(ma_sv, ho_ten, lop, gpa, diem_rl)
    ql.them_sinh_vien(sv)


def main():
    ql = QuanLySinhVien()

    while True:
        print("\n===== QUAN LY SINH VIEN - TV2 =====")
        print("1. Them sinh vien")
        print("2. Sua sinh vien")
        print("3. Xoa sinh vien")
        print("4. Tim kiem sinh vien")
        print("5. Hien thi danh sach")
        print("0. Thoat")

        chon = input("Nhap lua chon: ").strip()

        if chon == "1":
            them_sinh_vien(ql)

        elif chon == "2":
            ma_sv = input("Nhap ma sinh vien can sua: ")
            ql.sua_sinh_vien(ma_sv)

        elif chon == "3":
            ma_sv = input("Nhap ma sinh vien can xoa: ")
            ql.xoa_sinh_vien(ma_sv)

        elif chon == "4":
            tu_khoa = input("Nhap ma, ten hoac lop can tim: ")
            ql.tim_kiem(tu_khoa)

        elif chon == "5":
            ql.hien_thi()

        elif chon == "0":
            print("Ket thuc chuong trinh!")
            break

        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()
