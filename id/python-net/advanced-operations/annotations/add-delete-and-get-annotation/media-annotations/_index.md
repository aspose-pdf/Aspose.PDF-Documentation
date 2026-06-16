---
title: Anotasi Media dalam PDF
linktitle: Anotasi Media
type: docs
weight: 40
url: /id/python-net/media-annotations/
description: Pelajari cara menambahkan anotasi suara, 3D, layar, dan media kaya ke dokumen PDF, serta cara memeriksa atau menghapus anotasi multimedia menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Bekerja dengan anotasi PDF multimedia dan media kaya di Python.
Abstract: Artikel ini menjelaskan cara membuat dan mengelola anotasi media dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Artikel ini mencakup anotasi suara, anotasi 3D, anotasi layar, anotasi media kaya, serta teknik untuk menampilkan daftar atau menghapus anotasi multimedia dari halaman PDF.
---

Artikel ini menunjukkan cara bekerja dengan anotasi media dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET.

Script contoh menunjukkan beberapa alur kerja multimedia:

- tambahkan anotasi suara
- buat anotasi 3D dari model U3D
- tambahkan anotasi layar dari file media
- tambahkan dan hapus anotasi media kaya
- memeriksa anotasi multimedia yang ada

## Tambahkan Anotasi Suara

Contoh ini menambahkan anotasi suara ke halaman pertama PDF yang sudah ada dan menautkannya ke file media WAV yang disimpan di direktori input.

### Buka PDF dan tentukan file media

```python
media_dir = path.dirname(infile)

document = ap.Document(infile)
page = document.pages[1]

media_file = path.join(media_dir, "file_example_WAV_1MG.wav")
```

### Buat dan konfigurasikan anotasi suara

Atur persegi panjang anotasi, warna, judul, dan subjek. Kemudian tambahkan anotasi popup untuk memberikan detail tambahan saat anotasi dipilih.

```python
sound_annotation = ann.SoundAnnotation(
    page,
    ap.Rectangle(20, 700, 60, 740, True),
    media_file,
)

sound_annotation.color = ap.Color.blue
sound_annotation.title = "John Smith"
sound_annotation.subject = "Sound Annotation demo"

sound_annotation.popup = ann.PopupAnnotation(
    page,
    ap.Rectangle(20, 700, 60, 740, True),
)
```

### Tambahkan anotasi dan simpan PDF

```python
page.annotations.append(sound_annotation)
document.save(outfile)
```

### Contoh lengkap

```python
def sound_annotation_add(infile, outfile):
    media_dir = path.dirname(infile)

    document = ap.Document(infile)
    page = document.pages[1]

    media_file = path.join(media_dir, "file_example_WAV_1MG.wav")

    sound_annotation = ann.SoundAnnotation(
        page,
        ap.Rectangle(20, 700, 60, 740, True),
        media_file,
    )

    sound_annotation.color = ap.Color.blue
    sound_annotation.title = "John Smith"
    sound_annotation.subject = "Sound Annotation demo"

    sound_annotation.popup = ann.PopupAnnotation(
        page,
        ap.Rectangle(20, 700, 60, 740, True),
    )

    page.annotations.append(sound_annotation)
    document.save(outfile)
```

## Tambahkan Anotasi 3D

Alur kerja ini membuat PDF baru dan menyematkan model 3D dari file U3D. Ini juga mendefinisikan tampilan preset dan pengaturan rendering untuk konten 3D.

### Buat dokumen PDF dan konten 3D

```python
model_file = infile

document = ap.Document()

pdf3d_content = ann.PDF3DContent(model_file)
pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")
```

### Definisikan matriks tampilan 3D

Matriks-matriks ini menjelaskan bagaimana model 3D ditampilkan dari berbagai sudut pandang.

```python
top_matrix = ap.Matrix3D(
    1,
    0,
    0,
    0,
    -1,
    0,
    0,
    0,
    -1,
    0.10271,
    0.08184,
    0.273836,
)

front_matrix = ap.Matrix3D(
    0,
    -1,
    0,
    0,
    0,
    1,
    -1,
    0,
    0,
    0.332652,
    0.08184,
    0.085273,
)
```

### Tambahkan tampilan bernama ke karya seni

```python
pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
pdf3d_artwork.view_array.add(ann.PDF3DView(document, front_matrix, 0.188563, "Left"))
```

### Buat anotasi dan simpan dokumen

```python
page = document.pages.add()

pdf3d_annotation = ann.PDF3DAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 700, True),
    pdf3d_artwork,
)

pdf3d_annotation.border = ann.Border(pdf3d_annotation)
pdf3d_annotation.set_default_view_index(1)
pdf3d_annotation.flags = ann.AnnotationFlags.NO_ZOOM
pdf3d_annotation.name = path.basename(model_file)

page.annotations.append(pdf3d_annotation)
document.save(outfile)
```

### Contoh lengkap

```python
def annotation_3d_add(infile, outfile):
    model_file = infile

    document = ap.Document()

    pdf3d_content = ann.PDF3DContent(model_file)
    pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
    pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
    pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")

    top_matrix = ap.Matrix3D(
        1,
        0,
        0,
        0,
        -1,
        0,
        0,
        0,
        -1,
        0.10271,
        0.08184,
        0.273836,
    )

    front_matrix = ap.Matrix3D(
        0,
        -1,
        0,
        0,
        0,
        1,
        -1,
        0,
        0,
        0.332652,
        0.08184,
        0.085273,
    )

    pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
    pdf3d_artwork.view_array.add(
        ann.PDF3DView(document, front_matrix, 0.188563, "Left")
    )

    page = document.pages.add()

    pdf3d_annotation = ann.PDF3DAnnotation(
        page,
        ap.Rectangle(100, 500, 300, 700, True),
        pdf3d_artwork,
    )

    pdf3d_annotation.border = ann.Border(pdf3d_annotation)
    pdf3d_annotation.set_default_view_index(1)
    pdf3d_annotation.flags = ann.AnnotationFlags.NO_ZOOM
    pdf3d_annotation.name = path.basename(model_file)

    page.annotations.append(pdf3d_annotation)
    document.save(outfile)
```

## Tambahkan Anotasi Layar

Anotasi layar memungkinkan Anda menempelkan media yang dapat diputar ke halaman PDF. Contoh ini membuat PDF baru dan menambahkan anotasi layar berdasarkan file SWF.

### Buat PDF dan halaman

```python
media_file = infile

document = ap.Document()
page = document.pages.add()
```

### Buat anotasi layar

```python
screen_annotation = ann.ScreenAnnotation(
    page,
    ap.Rectangle(170, 190, 470, 380, True),
    media_file,
)
```

### Tambahkan anotasi dan simpan PDF

```python
page.annotations.append(screen_annotation)
document.save(outfile)
```

### Contoh lengkap

```python
def screen_annotation_with_media_add(infile, outfile):
    media_file = infile

    document = ap.Document()
    page = document.pages.add()

    screen_annotation = ann.ScreenAnnotation(
        page,
        ap.Rectangle(170, 190, 470, 380, True),
        media_file,
    )

    page.annotations.append(screen_annotation)
    document.save(outfile)
```

## Anotasi Media Kaya

### Tambahkan Anotasi Media Kaya

Anotasi media kaya dapat menyematkan konten interaktif lanjutan seperti pemutar video dengan poster, skin, dan pengaturan pemutaran khusus.

### Siapkan media dan sumber daya pemutar

Contoh memuat video, gambar poster, dan file skin pemutar dari lokasi yang telah ditentukan.

```python
media_dir = path.dirname(infile)
path_to_adobe_app = (
    r"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins"
)

document = ap.Document()
page = document.pages.add()

video_name = "file_example_MP4_480_1_5MG.mp4"
poster_name = "file_example_MP4_480_1_5MG_poster.jpg"
skin_name = "SkinOverAllNoFullNoCaption.swf"
```

### Buat anotasi media kaya

```python
rich_media_annotation = ann.RichMediaAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 600, True),
)
```

### Lampirkan pemutar khusus, skin, poster, dan video

```python
player_path = os.path.join(path_to_adobe_app, "Players", "Videoplayer.swf")
rich_media_annotation.custom_player = open(player_path, "rb")
rich_media_annotation.custom_flash_variables = f"source={video_name}&skin={skin_name}"

skin_path = os.path.join(path_to_adobe_app, skin_name)
rich_media_annotation.add_custom_data(skin_name, open(skin_path, "rb"))

poster_path = os.path.join(media_dir, poster_name)
rich_media_annotation.set_poster(open(poster_path, "rb"))

video_path = os.path.join(media_dir, video_name)
with open(video_path, "rb") as video_file:
    rich_media_annotation.set_content(video_name, video_file)
```

### Atur perilaku pemutaran dan simpan PDF

Anotasi dikonfigurasi sebagai konten video dan diaktifkan ketika pengguna mengkliknya.

```python
rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

rich_media_annotation.update()

page.annotations.append(rich_media_annotation)
document.save(outfile)
```

### Contoh lengkap

```python
def rich_media_annotations_add(infile, outfile):
    media_dir = path.dirname(infile)
    path_to_adobe_app = (
        r"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins"
    )

    document = ap.Document()
    page = document.pages.add()

    video_name = "file_example_MP4_480_1_5MG.mp4"
    poster_name = "file_example_MP4_480_1_5MG_poster.jpg"
    skin_name = "SkinOverAllNoFullNoCaption.swf"

    rich_media_annotation = ann.RichMediaAnnotation(
        page,
        ap.Rectangle(100, 500, 300, 600, True),
    )

    player_path = os.path.join(path_to_adobe_app, "Players", "Videoplayer.swf")
    rich_media_annotation.custom_player = open(player_path, "rb")
    rich_media_annotation.custom_flash_variables = (
        f"source={video_name}&skin={skin_name}"
    )

    skin_path = os.path.join(path_to_adobe_app, skin_name)
    rich_media_annotation.add_custom_data(skin_name, open(skin_path, "rb"))

    poster_path = os.path.join(media_dir, poster_name)
    rich_media_annotation.set_poster(open(poster_path, "rb"))

    video_path = os.path.join(media_dir, video_name)
    with open(video_path, "rb") as video_file:
        rich_media_annotation.set_content(video_name, video_file)

    rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
    rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

    rich_media_annotation.update()

    page.annotations.append(rich_media_annotation)
    document.save(outfile)
```

### Hapus Anotasi Media Kaya

Alur kerja ini menghapus semua anotasi media kaya dari halaman pertama PDF yang ada.

### Buka PDF dan kumpulkan anotasi media kaya

```python
document = ap.Document(infile)
page = document.pages[1]

to_delete = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
]
```

### Hapus anotasi dan simpan dokumen

```python
for annotation in to_delete:
    page.annotations.delete(annotation)

document.save(outfile)
```

### Contoh lengkap

```python
def rich_media_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    to_delete = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
    ]

    for annotation in to_delete:
        page.annotations.delete(annotation)

    document.save(outfile)
```

## Ambil Multimedia_annotations

Untuk memeriksa konten multimedia yang sudah disimpan dalam PDF, filter koleksi anotasi untuk tipe anotasi layar, suara, dan media kaya.

### Buka dokumen dan tentukan jenis anotasi target

```python
document = ap.Document(infile)

target_types = {
    ann.AnnotationType.SCREEN,
    ann.AnnotationType.SOUND,
    ann.AnnotationType.RICH_MEDIA,
}
```

### Cetak persegi panjang anotasi multimedia

```python
for annotation in document.pages[1].annotations:
    if annotation.annotation_type in target_types:
        print(f"{annotation.annotation_type} [{annotation.rect}]")
```

### Contoh lengkap

```python
def multimedia_annotations_get(infile, outfile):
    document = ap.Document(infile)

    target_types = {
        ann.AnnotationType.SCREEN,
        ann.AnnotationType.SOUND,
        ann.AnnotationType.RICH_MEDIA,
    }

    for annotation in document.pages[1].annotations:
        if annotation.annotation_type in target_types:
            print(f"{annotation.annotation_type} [{annotation.rect}]")
```

## Topik Terkait

- [Impor dan Ekspor Anotasi](/python-net/import-export-annotations/)
- [Anotasi Interaktif](/python-net/interactive-annotations/)
- [Anotasi Penandaan](/python-net/markup-annotations/)
- [Anotasi Keamanan](/python-net/security-annotations/)
- [Anotasi Bentuk](/python-net/shape-annotations/)
- [Anotasi Berbasis Teks](/python-net/text-based-annotations/)
- [Anotasi Watermark](/python-net/watermark-annotations/)
