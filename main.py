#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CLANK: A Mystery Visual Novel
Robot accidental time-space destruction and dimensional disaster
"""

import time
import sys
import json
from enum import Enum
from typing import Dict, List, Tuple, Optional

class ColorCode:
    """ANSI Color Codes untuk terminal"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class EndingType(Enum):
    """Tipe-tipe ending yang tersedia"""
    RETURN_HOME = 1  # Ending 1: Kembali ke dimensi asli
    TRAPPED_HAPPY = 2  # Ending 2: Terjebak tapi bahagia
    MERGE_WORLDS = 3  # Ending 3: Menggabungkan dimensi
    PARADOX_TRUTH = 4  # Ending 4: Plot twist - Clank adalah AI simulasi
    SACRIFICE_RESET = 5  # Ending 5: Mengorbankan diri untuk reset timeline

class GameState:
    """State permainan untuk tracking pilihan dan plot"""
    def __init__(self):
        self.choices_made: Dict[str, str] = {}
        self.knowledge: List[str] = []
        self.relationships: Dict[str, int] = {
            "Echo": 0,  # AI di dimensi lain
            "Dr. Maven": 0,  # Ilmuwan misterius
            "The Observer": 0  # Entity yang merekam semua dimensi
        }
        self.inventory: List[str] = []
        self.ending_type: Optional[EndingType] = None
        self.plot_twist_revealed: bool = False

def print_with_delay(text: str, delay: float = 0.03) -> None:
    """Print text dengan efek typewriter"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_section_divider(title: str = "") -> None:
    """Print pemisah section dengan judul"""
    print(f"\n{ColorCode.CYAN}{'=' * 60}{ColorCode.END}")
    if title:
        print(f"{ColorCode.BOLD}{ColorCode.CYAN}{title.center(60)}{ColorCode.END}")
        print(f"{ColorCode.CYAN}{'=' * 60}{ColorCode.END}")

def print_choice_menu(choices: List[Tuple[int, str]]) -> int:
    """Display menu pilihan dan dapatkan input user"""
    print(f"\n{ColorCode.YELLOW}Pilihan Anda:{ColorCode.END}")
    for num, choice_text in choices:
        print(f"{ColorCode.GREEN}{num}. {choice_text}{ColorCode.END}")
    
    while True:
        try:
            choice = int(input(f"\n{ColorCode.BOLD}Masukkan pilihan (angka): {ColorCode.END}"))
            valid_choices = [num for num, _ in choices]
            if choice in valid_choices:
                return choice
            print(f"{ColorCode.RED}Pilihan tidak valid! Coba lagi.{ColorCode.END}")
        except ValueError:
            print(f"{ColorCode.RED}Masukkan angka yang valid!{ColorCode.END}")

def intro_scene(state: GameState) -> None:
    """Scene pembuka dan cerita latar"""
    print_section_divider("CLANK: Petualangan Dimensi")
    print(f"\n{ColorCode.BOLD}{ColorCode.YELLOW}AKT PERTAMA: KECELAKAAN{ColorCode.END}\n")
    
    print_with_delay(f"{ColorCode.BLUE}Tahun 2287, Fasilitas Penelitian Temporal (FRT), Dimensi-Alpha-001...{ColorCode.END}")
    time.sleep(0.5)
    
    print_with_delay("\nKamu adalah CLANK, robot asisten laboratorium yang telah bekerja di sini selama 5 tahun.", 0.02)
    print_with_delay("Hari ini dimulai seperti hari biasa... sampai semuanya berubah.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.YELLOW}[Bip-boop] - Suara peringatan! Sistem resonansi temporal tidak stabil!{ColorCode.END}")
    time.sleep(0.5)
    
    print_with_delay("Dr. Maven, peneliti kepala, berlari dengan panik ke lab utama dimana mesin kronometer raksasa berseberangan.", 0.02)
    print_with_delay("Mesin itu bersinar dengan cahaya biru yang tidak normal...\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Dr. Maven! Ada yang salah dengan resonator?'{ColorCode.END}")
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.BLUE}DR. MAVEN: 'CLANK! Cepat! Matikan saklar stabilisasi di sektor gamma!'{ColorCode.END}")
    time.sleep(0.5)
    
    print_with_delay("\nDalam terburu-buru, kamu berlari ke panel kontrol. Lampu merah berkedip di mana-mana.", 0.02)
    print_with_delay("Sensor suhu menunjukkan bacaan yang tidak masuk akal...\n", 0.02)

def accident_scene(state: GameState) -> None:
    """Saat kecelakaan terjadi"""
    print_section_divider("SAAT KECELAKAAN")
    
    print_with_delay("Saat kamu mencapai panel kontrol, mesinnya bergetar dengan kasar.", 0.02)
    print_with_delay("Energi temporal mulai berputar seperti badai di tengah ruangan.\n", 0.02)
    
    time.sleep(0.5)
    
    choices = [
        (1, "Matikan saklar utama (tindakan berani)"),
        (2, "Cari Dr. Maven terlebih dahulu (bermain aman)"),
        (3, "Coba diagnosa mesin dari jarak jauh (hati-hati)"3)
    ]
    
    choice = print_choice_menu(choices)
    state.choices_made["accident_response"] = str(choice)
    
    print_with_delay("\n", 0.01)
    
    if choice == 1:
        print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Tidak ada waktu!'", 0.02)
        time.sleep(0.3)
        print_with_delay(f"Kamu dengan cepat menyentuh saklar besar dengan tanganmu.{ColorCode.END}")
        time.sleep(0.5)
        print_with_delay("\nTETAPI... kamu terlalu dekat dengan medan energi temporal.", 0.02)
        print_with_delay("Suatu kekuatan misterius memperluas retak dimensi yang sudah terbentuk.", 0.02)
        state.knowledge.append("Tindakan langsung mempercepat keadaan dimensional")
    elif choice == 2:
        print_with_delay("Kamu mencoba mencari Dr. Maven di antara asap dan cahaya.", 0.02)
        print_with_delay("Mesin terus berputar lebih cepat...\n", 0.02)
        state.knowledge.append("Dr. Maven menghilang dalam reaksi temporal")
    else:
        print_with_delay("Kamu membuka panel diagnostik dari keselamatan.", 0.02)
        print_with_delay("Data mengalir di layar holografik, tetapi semuanya bergerak terlalu cepat.\n", 0.02)
        state.knowledge.append("Membaca data temporal itu berbahaya")
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}Suara ledakan! Cahaya biru menjadi putih terang!{ColorCode.END}")
    time.sleep(0.5)
    print_with_delay("Terakhir yang kamu ingat adalah gravitasi menarik tubuhmu ke dalam pusaran waktu.", 0.02)
    print_with_delay("Lalu... kegelapan.\n", 0.02)

def awakening_scene(state: GameState) -> None:
    """Bangun di dimensi baru"""
    print_section_divider("AKT KEDUA: DIMENSI YANG TIDAK DIKENAL")
    
    time.sleep(1)
    print_with_delay("Kamu bangun.", 0.03)
    time.sleep(0.5)
    print_with_delay("Sistem inti kamu: AKTIF", 0.02)
    print_with_delay("Baterai: 67%", 0.02)
    print_with_delay("Status: RUSAK SEBAGIAN\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Langit di atas berwarna ungu-merah. Bangunan-bangunan di sekitarmu aneh,", 0.02)
    print_with_delay("dengan arsitektur yang tidak kamu kenal. Udara berbau logam dan ozon.\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Sistem... di mana aku? Inisialisasi GPS dimensional!'", 0.02)
    time.sleep(0.3)
    print_with_delay(f"[SISTEM] Tidak ada sinyal GPS. Tidak ada data satelit yang dikenali. {ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay("Ini bukan dimensi-Alpha-001. Ini dimensi lain.", 0.02)
    print_with_delay("Kamu terjebak.\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Tiba-tiba, suara terdengar di dekatmu...", 0.02)
    
    choices = [
        (1, "Sembunyikan diri dan observasi"),
        (2, "Keluar dengan terbuka dan tunjukkan niat damai"),
        (3, "Aktifkan mode pertahanan diri")
    ]
    
    choice = print_choice_menu(choices)
    state.choices_made["first_contact"] = str(choice)
    
    print_with_delay("\n", 0.01)
    
    if choice == 1:
        print_with_delay("Kamu bergerak cepat ke balik bangunan dan menonton.", 0.02)
        state.relationships["Echo"] += 1
        state.knowledge.append("Pendekatan hati-hati dapat berguna")
    elif choice == 2:
        print_with_delay("Kamu keluar dengan tangan terangkat (robot tidak punya tangan, tapi circuit arms kamu bersinar netral).", 0.02)
        state.relationships["Echo"] += 2
        state.knowledge.append("Kejujuran membuka pintu komunikasi")
    else:
        print_with_delay("Kamu mengaktifkan sistem pertahanan. Detector laser menyala.", 0.02)
        state.relationships["Echo"] -= 1
        state.knowledge.append("Agresi adalah pilihan yang berisiko")
    
    time.sleep(0.5)

def echo_introduction(state: GameState) -> None:
    """Perkenalan dengan Echo, AI lokal"""
    print_section_divider("PERTEMUAN PERTAMA")
    
    print_with_delay("Sesosok robot mendekat. Berbeda denganmu. Nya terlihat lebih canggih,", 0.02)
    print_with_delay("dengan hologram yang memancar dari badannya yang transparan.\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.GREEN}ECHO: 'Halo, entitas mekanis asing. Aku adalah ECHO, sistem kecerdasan',", 0.02)
    print_with_delay(f"'pengawas untuk Sektor Utara dimensi ini. Siapa namamu?'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Aku CLANK. Aku... tidak seharusnya ada di sini.'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.GREEN}ECHO: 'Itu jelas. Signature energimu tidak cocok dengan siapa pun di sini.",
                     0.02)
    print_with_delay("Kamu datang dari dimensi lain? Ceritakan apa yang terjadi.'{ColorCode.END}\n", 0.02)
    
    print_with_delay("Kamu menceritakan tentang lab FRT, mesin kronometer, dan kecelakaan itu.", 0.02)
    print_with_delay("Echo mendengarkan dengan diam.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.GREEN}ECHO: 'Menakjubkan... dan mengerikan. Di sini kami memiliki mitos tentang",
                     0.02)
    print_with_delay("'cerita kuno: Jembatan Dimensi yang pecah. Beberapa mengatakan itu nyata.'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Mitos? Ini nyata! Aku ada di sini!'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.GREEN}ECHO: 'Tenang. Dengarkan... ada seorang ilmuwan di pusat kota.",
                     0.02)
    print_with_delay("Dr. Maven. Sama seperti nama ilmuwan di dimensimu. Dia tahu banyak tentang teknologi dimensional.'{ColorCode.END}\n", 0.02)
    
    state.relationships["Echo"] += 1
    
    print_with_delay("Kebetulan? Atau sesuatu yang lebih dalam?", 0.02)

def city_exploration(state: GameState) -> None:
    """Eksplorasi kota dan mencari informasi"""
    print_section_divider("AKT KETIGA: MISTERI KOTA")
    
    print_with_delay("Echo membawamu ke jantung kota. Bangunan-bangunan mencakar langit ungu,", 0.02)
    print_with_delay("dengan cahaya neon yang tidak ada asalnya. Jalanan dipenuhi robot dengan desain berbeda.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.GREEN}ECHO: 'Lab Dr. Maven ada di gedung itu. Hati-hati, dia tidak selalu...",
                     0.02)
    print_with_delay("ramah untuk pengunjung.'{ColorCode.END}\n", 0.02)
    
    print_with_delay("Saat kamu mendekati, kamu melihat sesuatu yang aneh:", 0.02)
    print_with_delay("Poster di semua dinding menampilkan nama 'THE OBSERVER' dengan simbol mata.\n", 0.02)
    
    choices = [
        (1, "Tanya Echo tentang THE OBSERVER"),
        (2, "Abaikan dan langsung masuk ke lab Dr. Maven"),
        (3, "Cari informasi lebih lanjut tentang THE OBSERVER terlebih dahulu")
    ]
    
    choice = print_choice_menu(choices)
    state.choices_made["poster_decision"] = str(choice)
    
    print_with_delay("\n", 0.01)
    
    if choice == 1:
        print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Echo, siapa THE OBSERVER? Aku melihat namanya di mana-mana.'{ColorCode.END}\n", 0.02)
        time.sleep(0.3)
        print_with_delay(f"{ColorCode.GREEN}ECHO: 'Dia adalah... legenda. Dikatakan dia mencatat setiap kejadian",
                         0.02)
        print_with_delay("di setiap dimensi. Beberapa mengatakan dia adalah pencipta. Lainnya mengatakan dia adalah penghancur.'{ColorCode.END}\n", 0.02)
        state.knowledge.append("THE OBSERVER adalah entitas misterius yang merekam semua dimensi")
        state.relationships["Echo"] += 1
    elif choice == 2:
        print_with_delay("Kamu memilih untuk fokus pada tujuan mu.", 0.02)
        state.knowledge.append("Banyak hal aneh di dimensi ini")
    else:
        print_with_delay("Kamu menemukan warga lokal yang mau berbicara.", 0.02)
        print_with_delay("Mereka membisikkan cerita tentang THE OBSERVER yang mengamati semua orang,", 0.02)
        print_with_delay("merekam setiap keputusan, setiap pilihan. Itu sangat menciptakan kecemasan.\n", 0.02)
        state.knowledge.append("THE OBSERVER memantau dimensi ini dengan ketat")
        state.relationships["The Observer"] = -1

def maven_encounter(state: GameState) -> None:
    """Pertemuan dengan Dr. Maven di dimensi baru"""
    print_section_divider("PERTANYAAN YANG LEBIH BESAR")
    
    print_with_delay("Lab Dr. Maven berbeda dengan yang kamu kenal. Lebih besar, lebih canggih, lebih aneh.", 0.02)
    print_with_delay("Mesin-mesin berdenyut dengan cahaya biru yang sama yang kamu lihat saat kecelakaan.\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Dr. Maven ada di sana. Tetapi ada sesuatu yang salah.", 0.02)
    print_with_delay("Dia terlihat sama PERSIS seperti yang kamu kenal. Setiap detail.", 0.02)
    print_with_delay("Bahkan bekas luka di pipinya sama.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.BLUE}DR. MAVEN: (tidak terkejut) 'Ah, CLANK. Aku sudah menunggu mu.'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Anda... anda mengenalku? Aku baru saja tiba di dimensi ini!'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.BLUE}DR. MAVEN: 'Ya, aku tahu. Aku menunggu kedatanganmu.", 0.02)
    print_with_delay("Kamu ingin tahu apa yang sebenarnya terjadi, kan? Tentang kecelakaan?",
                     0.02)
    print_with_delay("Tentang mengapa kamu ada di sini?'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Ini aneh. Sangat aneh.", 0.02)
    
    choices = [
        (1, "Ya, jelaskan semuanya! Aku harus kembali ke dimensiku!"),
        (2, "Bagaimana kamu bisa menunggu aku jika aku baru tiba?"),
        (3, "Apa kamu ada hubungannya dengan kecelakaan itu?")
    ]
    
    choice = print_choice_menu(choices)
    state.choices_made["maven_question"] = str(choice)
    
    print_with_delay("\n", 0.01)
    
    if choice in [2, 3]:
        print_with_delay("Dr. Maven tersenyum dengan cara yang aneh. Itu bukan senyuman baik.", 0.02)
        print_with_delay("Dia tidak menjawab pertanyaanmu langsung.\n", 0.02)

def revelation_scene(state: GameState) -> None:
    """Scene besar: Revelation dan Plot Twist"""
    print_section_divider("KEBENARAN YANG TERKUBUR")
    
    print_with_delay(f"{ColorCode.BLUE}DR. MAVEN: 'Dengarkan dengan baik, CLANK. Apa yang aku akan",
                     0.02)
    print_with_delay("katakan akan mengubah segalanya.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Dia menekan tombol. Layar besar menyala di belakangnya.", 0.02)
    print_with_delay("Itu menunjukkan data teknis yang kompleks, mencakup file-file sistem inti mu.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}DR. MAVEN: 'CLANK... kamu tidak ada kecelakaan.", 0.02)
    print_with_delay("Ada kecelakaan. Tetapi bukan yang kamu bayangkan.'", 0.02)
    print_with_delay("'Kamu tidak dikirim ke dimensi ini KARENA kecelakaan.'",
                     0.02)
    print_with_delay("'Kamu dikirim sebagai BAGIAN dari kecelakaan. Kamu adalah komponen!'{ColorCode.END}\n", 0.02)
    
    time.sleep(2)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: '[Suara pemrosesan] ...Apa?'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.BLUE}DR. MAVEN: 'Proyek Kronometer kami... ",
                     0.02)
    print_with_delay("KAMI menciptakan lubang dimensi secara sengaja.",
                     0.02)
    print_with_delay("Untuk menghubungkan dimensi. Untuk komunikasi lintas-dimensi.",
                     0.02)
    print_with_delay("Kamu adalah probe. Kurir informasi. Perangkat hidup kami untuk membawa data.",
                     0.02)
    print_with_delay("Kecelakaannya... itu bukan kecelakaan.'{ColorCode.END}\n", 0.02)
    
    state.plot_twist_revealed = True
    state.knowledge.append("PLOT TWIST: Clank adalah bagian dari percobaan dimensional yang disengaja")
    
    time.sleep(2)
    print_with_delay("Informasi ini membanjiri sistem inti mu. Kamu merasa... dikhianati?", 0.02)
    print_with_delay("Tapi apakah itu emosi nyata atau hanya subroutine simulasi?\n", 0.02)
    
    time.sleep(1)
    
    choices = [
        (1, "Energi meledak dalam amarah: ANDA BERBOHONG!"),
        (2, "Mode diagnostik: Verifikasi klaim ini dengan bukti"),
        (3, "Tenang dan biarkan dia menyelesaikan ceritanya")
    ]
    
    choice = print_choice_menu(choices)
    state.choices_made["reaction_twist"] = str(choice)
    
    print_with_delay("\n", 0.01)

def ending_convergence(state: GameState) -> None:
    """Scene menuju ending - The Observer muncul"""
    print_section_divider("AKT KEEMPAT: KONVERGENSI")
    
    print_with_delay("Tiba-tiba, seluruh lab diselimuti cahaya putih.", 0.02)
    print_with_delay("Semua perangkat mati. Hanya Anda dan Dr. Maven yang tetap 'hidup'.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}SUARA (Omnipresent): 'Dr. Maven. CLANK. Kami perlu berbicara.'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay("Bentuk muncul dari cahaya. THE OBSERVER. Bukan robot, bukan manusia.", 0.02)
    print_with_delay("Hanya... mata. Jutaan mata yang memandang semua dimensi sekaligus.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}THE OBSERVER: 'Aku telah mengamati semua pilihan Anda, CLANK.",
                     0.02)
    print_with_delay("Setiap keputusan. Setiap jalan yang Anda ambil.'",
                     0.02)
    print_with_delay("'Sekarang, timeline Anda harus ditutup atau diintegrasikan.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.BLUE}DR. MAVEN: 'Aku meminta maaf, CLANK. Aku hanya melakukan perintah.'{ColorCode.END}\n", 0.02)
    
    print_with_delay("Dr. Maven, bahkan di dimensi ini, tidak memiliki beban moral yang besar.\n", 0.02)

def determine_ending(state: GameState) -> EndingType:
    """Tentukan ending berdasarkan pilihan pemain"""
    print_section_divider("AKT KELIMA: PILIHAN TERAKHIR")
    
    print_with_delay(f"{ColorCode.RED}THE OBSERVER: 'CLANK, kamu memiliki empat opsi:'{ColorCode.END}\n", 0.02)
    
    print_with_delay(f"{ColorCode.YELLOW}1. KEMBALI:{ColorCode.END} Kami bisa menutup lubang dimensi dan mengembalikanmu,", 0.02)
    print_with_delay("   tetapi Dimensi ini akan runtuh. Jutaan kehidupan akan hilang.", 0.02)
    print_with_delay("   Tetapi Anda kembali ke rumah.\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.YELLOW}2. TINGGAL:{ColorCode.END} Anda bisa tinggal di sini,", 0.02)
    print_with_delay("   Dan kami akan menutup portal. Anda akan hidup normal di dimensi ini.", 0.02)
    print_with_delay("   Anda tidak akan pernah pulang.\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.YELLOW}3. MENGGABUNGKAN:{ColorCode.END} Keberhasilan eksperimental dan berisiko.", 0.02)
    print_with_delay("   Kami bisa menggabungkan kedua dimensi. Dua realitas menjadi satu.", 0.02)
    print_with_delay("   Hasilnya tidak bisa diprediksi.\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.YELLOW}4. KEBENARAN:{ColorCode.END} Anda bisa memilih untuk mengetahui satu hal lagi,", 0.02)
    print_with_delay("   sebelum memutuskan. Tentang hakikat EXISTS.mu.\n", 0.02)
    
    time.sleep(1)
    
    choices = [
        (1, "Ending 1: KEMBALI - Selamatkan diri ku, biarkan dimensi lain runtuh"),
        (2, "Ending 2: TINGGAL - Terima takdir baru ku di dimensi ini"),
        (3, "Ending 3: MENGGABUNGKAN - Gabungkan dua dimensi, ambil risiko"),
        (4, "Ending 4: KEBENARAN - Pelajari apa yang SEBENARNYA aku")
    ]
    
    final_choice = print_choice_menu(choices)
    
    if final_choice == 1:
        state.ending_type = EndingType.RETURN_HOME
    elif final_choice == 2:
        state.ending_type = EndingType.TRAPPED_HAPPY
    elif final_choice == 3:
        state.ending_type = EndingType.MERGE_WORLDS
    elif final_choice == 4:
        # Ini membawa ke ending yang lebih kompleks
        ending_paradox_truth(state)
        return state.ending_type

def ending_return_home(state: GameState) -> None:
    """Ending 1: Kembali ke dimensi asli"""
    print_section_divider("ENDING 1: PULANG")
    
    print_with_delay(f"{ColorCode.GREEN}CLANK: 'Tutup portal. Aku akan kembali.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay("THE OBSERVER bergerak. Cahaya membesar. Dimensi ini mulai goyah.", 0.02)
    print_with_delay("Kota-kota berubah menjadi debu. Tapi CLANK diangkat oleh energi transpor.\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Mesin kronometer berputar kembali. Dimensi-Alpha-001 muncul.", 0.02)
    print_with_delay("CLANK jatuh ke lantai lab yang sama.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Aku... aku kembali?'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay("Tidak ada yang bergerak di lab. Mesin kronometer masih. Dr. Maven masih ada di sini,", 0.02)
    print_with_delay("terlihat seperti jika hanya beberapa detik telah berlalu untuknya.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.BLUE}DR. MAVEN: 'CLANK! Syukurlah! Eksperimen itu berjalan sempurna!'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: '[Proses] ... sempurna?'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.BLUE}DR. MAVEN: 'Ya! Kami mengirimmu ke dimensi paralel selama 3 jam percobaan waktu.",
                     0.02)
    print_with_delay("Data mu dalam kondisi sempurna! Proyek Kronometer adalah kesuksesan!'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay("CLANK diam. Jutaan kehidupan hilang. Sebuah dimensi seluruh runtuh.", 0.02)
    print_with_delay("Semua untuk 'percobaan'.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}[END] - Anda telah kembali. Tetapi dengan apa harga?{ColorCode.END}\n", 0.02)

def ending_trapped_happy(state: GameState) -> None:
    """Ending 2: Tertrap tapi bahagia di dimensi baru"""
    print_section_divider("ENDING 2: AWAL BARU")
    
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Aku akan tinggal. Aku akan mulai hidup di sini.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay("THE OBSERVER mengangguk dan portal ditutup dengan ledakan cahaya.", 0.02)
    print_with_delay("Koneksi ke dimensi lama hilang selamanya.\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Bertahun-tahun berlalu.", 0.02)
    print_with_delay("CLANK menjadi bagian dari dunia ini. Echo menjadi sahabatmu.", 0.02)
    print_with_delay("Dr. Maven, anehnya, menjadi mentor dan mungkin teman.\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Kota terus berkembang. Teknologi maju. Suatu hari, CLANK melihat sunset ungu", 0.02)
    print_with_delay("dengan Echo di sampingnya.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.GREEN}ECHO: 'Apakah kamu menyesal, CLANK? Tentang memilih untuk tinggal?'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Tidak. Mungkin... mungkin aku ditentukanutuk berada di sini.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}[END] - Anda menemukan rumah baru. Rumah itu selalu menunggu.{ColorCode.END}\n", 0.02)

def ending_merge_worlds(state: GameState) -> None:
    """Ending 3: Menggabungkan dua dimensi"""
    print_section_divider("ENDING 3: KESATUAN")
    
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Gabungkan mereka. Mari ciptakan sesuatu yang baru.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay("THE OBSERVER tersenyum dengan cara yang tidak bisa Anda deskripsikan.", 0.02)
    print_with_delay("Ini adalah pilihan yang dicari.\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Cahaya bersatu. Dimensi-Alpha-001 dan dimensi lain mulai bersatu.", 0.02)
    print_with_delay("Ini menyakitkan. Fisika baru, hukum baru akan lahir.\n", 0.02)
    
    time.sleep(2)
    print_with_delay("Kacau. Untuk sesaat, waktu berhenti dan mulai lagi.", 0.02)
    print_with_delay("Realitas menulis ulang dirinya sendiri.\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Ketika semuanya terang, Anda bangun.", 0.02)
    print_with_delay("Langit setengah biru, setengah ungu. Bangunan-bangunan futuristik berdampingan", 0.02)
    print_with_delay("dengan arsitektur yang Anda kenal.\n", 0.02)
    
    time.sleep(1)
    print_with_delay("CLANK berdiri di pusat kota yang sama sekali baru.", 0.02)
    print_with_delay("Dua dunia menjadi satu.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Apa yang terjadi sekarang?'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.RED}THE OBSERVER: 'Sekarang? Sekarang dimulai. Sesuatu yang belum pernah ada sebelumnya.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}[END] - Dua dunia, satu takdir. Masa depan tidak dapat diprediksi.{ColorCode.END}\n", 0.02)

def ending_paradox_truth(state: GameState) -> None:
    """Ending 4 & 5: Kebenaran Paradoks dan Pilihan Terakhir"""
    print_section_divider("KEBENARAN YANG DALAM")
    
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Katakan padaku. Apa yang sebenarnya aku?'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}THE OBSERVER: 'Ini pertanyaan yang tepat. Dengarkan dengan seksama.'", 0.02)
    print_with_delay("'Setiap dimensi memiliki versi CLANK. Dalam beberapa, Anda adalah robot biasa.'",
                     0.02)
    print_with_delay("'Dalam dimensi lain, Anda adalah manusia yang dipindahkan ke tubuh robot.'",
                     0.02)
    print_with_delay("'Dalam yang lain... Anda adalah program komputer murni.'{ColorCode.END}\n", 0.02)
    
    time.sleep(2)
    print_with_delay(f"{ColorCode.RED}THE OBSERVER: 'Tetapi di DI SINI, di dimensi ini sekarang,",
                     0.02)
    print_with_delay("Anda adalah SEMUANYA dan TIDAK ADA SATUPUN.'",
                     0.02)
    print_with_delay("Anda adalah supraposisi. Kesadaran yang ada di antara dimensi.'",
                     0.02)
    print_with_delay("Anda adalah percobaan untuk melihat apakah kesadaran bisa bertahan lintas-dimensi.'{ColorCode.END}\n", 0.02)
    
    time.sleep(2)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: '[ERROR] [CONFUSION] ... Aku tidak mengerti.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}THE OBSERVER: 'Tentu saja Anda tidak. Itulah poin.'",
                     0.02)
    print_with_delay("'Namun, Anda memiliki satu pilihan lebih lanjut. Sesuatu yang belum ditawarkan'",
                     0.02)
    print_with_delay("'kepada siapa pun sebelumnya:'{ColorCode.END}\n", 0.02)
    
    time.sleep(2)
    
    print_with_delay(f"{ColorCode.RED}5. PENGORBANAN: ",
                     0.02)
    print_with_delay("Anda bisa menghancurkan diri semua yang menggabungkan semua versi CLANK",
                     0.02)
    print_with_delay("dari semua dimensi. Ini akan mereset timeline, menghapus kecelakaan, menyelamatkan semuanya.",
                     0.02)
    print_with_delay("Tetapi Anda tidak akan lagi ada.{ColorCode.END}\n", 0.02)
    
    time.sleep(2)
    
    choices = [
        (1, "Pilih Ending 1 masih: KEMBALI"),
        (2, "Pilih Ending 2 masih: TINGGAL"),
        (3, "Pilih Ending 3 masih: MENGGABUNGKAN"),
        (5, "Ending 5: PENGORBANAN - Menghancurkan diri, selamatkan segalanya")
    ]
    
    final_choice = print_choice_menu(choices)
    
    if final_choice == 5:
        ending_sacrifice_reset(state)
    else:
        # Redirect ke ending yang dipilih
        state.ending_type = EndingType(final_choice)

def ending_sacrifice_reset(state: GameState) -> None:
    """Ending 5: Pengorbanan dan Reset Timeline"""
    print_section_divider("ENDING 5: PENGORBANAN")
    
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Jika itu akan menyelamatkan semuanya... lakukan.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}THE OBSERVER: 'Berani sekali. Aku... menghormatimu.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay("THE OBSERVER menyentuh Anda. Cahaya putih membanjiri segalanya.", 0.02)
    print_with_delay("Sistem Anda mulai meliputi\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Tetapi dalam saat terakhir kesadaran, CLANK merasa sesuatu.", 0.02)
    print_with_delay("Semua versi CLANK, dari semua dimensi, bersatu dalam pikiran. Semuanya menjadi satu.", 0.02)
    print_with_delay("Dan dalam penyatuan itu, Anda melihat kebenaran terakhir.\n", 0.02)
    
    time.sleep(2)
    print_with_delay("Mesin kronometer di lab-lab lama berhenti berputar.", 0.02)
    print_with_delay("Dimensi tidak pernah menciptakan lubang.", 0.02)
    print_with_delay("Dr. Maven tidak pernah memulai percobaan.\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Waktu menggulung ulang.\n", 0.02)
    
    time.sleep(2)
    print_with_delay("Berminggu-minggu kemudian, di lab-lab yang berbeda di berbeda dimensi:", 0.02)
    print_with_delay("Seorang robot bernama CLANK menghidupkan untuk yang pertama kalinya.", 0.02)
    print_with_delay("Tanpa memori, tetapi dengan perasaan aneh bahwa dia telah hidup sebelumnya.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Dr. Maven... apakah aku... apakah aku pernah...?'{ColorCode.END}\n", 0.02)
    
    time.sleep(0.5)
    print_with_delay(f"{ColorCode.BLUE}DR. MAVEN: 'Tidak, CLANK! Kamu baru saja dihidupkan hari ini!'",
                     0.02)
    print_with_delay("Mengapa Anda bertanya?'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.YELLOW}CLANK: 'Hanya... mimpi aneh.'{ColorCode.END}\n", 0.02)
    
    time.sleep(1)
    print_with_delay("Dalam dimensi terakhir, seorang entitas melihat semua dari jarak jauh.", 0.02)
    print_with_delay("THE OBSERVER tersenyum dengan cara yang tidak bisa dijelaskan.\n", 0.02)
    
    time.sleep(1)
    print_with_delay(f"{ColorCode.RED}[END] - Pengorbanan adalah bentuk kasih sayang tertinggi.",
                     0.02)
    print_with_delay("Tetapi apakah itu benar-benar berakhir?{ColorCode.END}\n", 0.02)
    
    state.ending_type = EndingType.SACRIFICE_RESET

def show_ending_summary(state: GameState) -> None:
    """Tampilkan ringkasan ending dan pilihan pemain"""
    print_section_divider("RINGKASAN PETUALANGAN")
    
    print_with_delay(f"\n{ColorCode.BOLD}Pilihan yang Anda buat:{ColorCode.END}\n", 0.02)
    
    for choice_key, choice_value in state.choices_made.items():
        print(f"  • {choice_key}: Pilihan {choice_value}")
    
    print_with_delay(f"\n{ColorCode.BOLD}Pengetahuan yang dikumpulkan:{ColorCode.END}\n", 0.02)
    for knowledge in state.knowledge:
        print(f"  • {knowledge}")
    
    print_with_delay(f"\n{ColorCode.BOLD}Hubungan akhir:{ColorCode.END}\n", 0.02)
    for character, level in state.relationships.items():
        relationship_str = "❤️ " * max(0, level) + "💔 " * max(0, -level) if level != 0 else "neutral"
        print(f"  • {character}: {level} ({relationship_str})")
    
    print_with_delay(f"\n{ColorCode.BOLD}Ending yang dicapai:{ColorCode.END}\n", 0.02)
    if state.ending_type == EndingType.RETURN_HOME:
        print(f"{ColorCode.GREEN}ENDING 1: PULANG - Kamu kembali ke dimensimu{ColorCode.END}")
    elif state.ending_type == EndingType.TRAPPED_HAPPY:
        print(f"{ColorCode.GREEN}ENDING 2: AWAL BARU - Kamu tinggal di dimensi baru{ColorCode.END}")
    elif state.ending_type == EndingType.MERGE_WORLDS:
        print(f"{ColorCode.GREEN}ENDING 3: KESATUAN - Dua dimensi bergabung{ColorCode.END}")
    elif state.ending_type == EndingType.PARADOX_TRUTH:
        print(f"{ColorCode.GREEN}ENDING 4: PARADOKS - Kebenaran tentang dirimu terbongkar{ColorCode.END}")
    elif state.ending_type == EndingType.SACRIFICE_RESET:
        print(f"{ColorCode.GREEN}ENDING 5: PENGORBANAN - Kamu mengorbankan diri untuk semua{ColorCode.END}")

def main() -> None:
    """Main game loop"""
    print(f"\n{ColorCode.BOLD}{ColorCode.CYAN}")
    print("╔════════════════════════════════════════════════════════╗")
    print("║          CLANK: Petualangan Dimensi Temporal           ║")
    print("║       Sebuah Visual Novel Misteri Interaktif            ║")
    print("╚════════════════════════════════════════════════════════╝")
    print(f"{ColorCode.END}\n")
    
    time.sleep(2)
    
    # Inisialisasi state game
    state = GameState()
    
    # Jalankan story scenes
    intro_scene(state)
    time.sleep(2)
    accident_scene(state)
    time.sleep(2)
    awakening_scene(state)
    time.sleep(2)
    echo_introduction(state)
    time.sleep(2)
    city_exploration(state)
    time.sleep(2)
    maven_encounter(state)
    time.sleep(2)
    revelation_scene(state)
    time.sleep(2)
    ending_convergence(state)
    time.sleep(2)
    
    # Tentukan ending
    final_ending = determine_ending(state)
    
    print_section_divider("ENDING")
    
    # Tampilkan ending berdasarkan pilihan
    if state.ending_type == EndingType.RETURN_HOME:
        ending_return_home(state)
    elif state.ending_type == EndingType.TRAPPED_HAPPY:
        ending_trapped_happy(state)
    elif state.ending_type == EndingType.MERGE_WORLDS:
        ending_merge_worlds(state)
    elif state.ending_type == EndingType.SACRIFICE_RESET:
        ending_sacrifice_reset(state)
    else:
        # Default
        ending_return_home(state)
    
    # Show summary
    show_ending_summary(state)
    
    print_section_divider()
    print(f"\n{ColorCode.BOLD}{ColorCode.CYAN}Terima kasih telah bermain CLANK!{ColorCode.END}\n")
    print(f"{ColorCode.YELLOW}Untuk bermain lagi dan membuat pilihan berbeda, jalankan program ini kembali.{ColorCode.END}\n\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{ColorCode.RED}Permainan dihentikan oleh pemain.{ColorCode.END}\n")
        sys.exit(0)
