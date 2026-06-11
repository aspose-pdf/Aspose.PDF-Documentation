---
title: التعليقات التوضيحية للوسائط في PDF
linktitle: التعليقات التوضيحية لوسائل الإعلام
type: docs
weight: 40
url: /ar/python-net/media-annotations/
description: تعرف على كيفية إضافة التعليقات التوضيحية الصوتية والثلاثية الأبعاد والشاشة والوسائط الغنية إلى مستندات PDF، وكيفية فحص التعليقات التوضيحية للوسائط المتعددة أو حذفها باستخدام Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: اعمل مع التعليقات التوضيحية للوسائط المتعددة والوسائط الغنية بصيغة PDF في Python.
Abstract: تشرح هذه المقالة كيفية إنشاء التعليقات التوضيحية للوسائط وإدارتها في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي التعليقات التوضيحية الصوتية والتعليقات التوضيحية ثلاثية الأبعاد والتعليقات التوضيحية للشاشة والتعليقات التوضيحية للوسائط الغنية وتقنيات إدراج التعليقات التوضيحية للوسائط المتعددة أو حذفها من صفحة PDF.
---

توضح هذه المقالة كيفية التعامل مع التعليقات التوضيحية للوسائط في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET.

يوضح البرنامج النصي النموذجي العديد من عمليات سير عمل الوسائط المتعددة:

- إضافة تعليق توضيحي صوتي
- إنشاء تعليق توضيحي ثلاثي الأبعاد من نموذج U3D
- إضافة تعليق توضيحي للشاشة من ملف وسائط
- إضافة التعليقات التوضيحية للوسائط الغنية وحذفها
- فحص التعليقات التوضيحية للوسائط المتعددة الموجودة

## إضافة تعليقات صوتية

يضيف هذا المثال تعليقًا توضيحيًا صوتيًا إلى الصفحة الأولى من ملف PDF موجود ويربطه بملف وسائط WAV المخزن في دليل الإدخال.

### افتح PDF وحدد ملف الوسائط

```python
media_dir = path.dirname(infile)

document = ap.Document(infile)
page = document.pages[1]

media_file = path.join(media_dir, "file_example_WAV_1MG.wav")
```

### إنشاء التعليق الصوتي وتكوينه

قم بتعيين مستطيل التعليق التوضيحي واللون والعنوان والموضوع. ثم أضف تعليقًا توضيحيًا منبثقًا لتوفير تفاصيل إضافية عند تحديد التعليق التوضيحي.

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

### أضف التعليق التوضيحي واحفظ ملف PDF

```python
page.annotations.append(sound_annotation)
document.save(outfile)
```

### مثال كامل

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

## إضافة تعليقات توضيحية ثلاثية الأبعاد

يقوم سير العمل هذا بإنشاء PDF جديد ويقوم بتضمين نموذج ثلاثي الأبعاد من ملف U3D. كما تحدد أيضًا طرق العرض المعدة مسبقًا وإعدادات العرض للمحتوى ثلاثي الأبعاد.

### قم بإنشاء مستند PDF ومحتوى ثلاثي الأبعاد

```python
model_file = infile

document = ap.Document()

pdf3d_content = ann.PDF3DContent(model_file)
pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(type_name="CAD")
pdf3d_artwork.render_mode = ann.PDF3DRenderMode(type_name="Solid")
```

### حدد مصفوفات العرض ثلاثي الأبعاد

تصف هذه المصفوفات كيفية عرض النموذج الثلاثي الأبعاد من وجهات نظر مختلفة.

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

### إضافة طرق عرض مسماة إلى العمل الفني

```python
pdf3d_artwork.view_array.add(ann.PDF3DView(document, top_matrix, 0.188563, "Top"))
pdf3d_artwork.view_array.add(ann.PDF3DView(document, front_matrix, 0.188563, "Left"))
```

### قم بإنشاء التعليق التوضيحي وحفظ المستند

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

### مثال كامل

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

## إضافة تعليقات توضيحية على الشاشة

تتيح لك التعليقات التوضيحية للشاشة إرفاق وسائط قابلة للتشغيل بصفحة PDF. يقوم هذا المثال بإنشاء ملف PDF جديد وإضافة تعليق توضيحي للشاشة استنادًا إلى ملف SWF.

### قم بإنشاء ملف PDF والصفحة

```python
media_file = infile

document = ap.Document()
page = document.pages.add()
```

### قم بإنشاء التعليق التوضيحي للشاشة

```python
screen_annotation = ann.ScreenAnnotation(
    page,
    ap.Rectangle(170, 190, 470, 380, True),
    media_file,
)
```

### أضف التعليق التوضيحي واحفظ ملف PDF

```python
page.annotations.append(screen_annotation)
document.save(outfile)
```

### مثال كامل

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

## التعليقات التوضيحية للوسائط الغنية

### إضافة تعليقات توضيحية للوسائط الغنية

يمكن للتعليقات التوضيحية للوسائط الغنية تضمين محتوى تفاعلي متقدم مثل مشغلات الفيديو مع الملصقات والجلود وإعدادات التشغيل المخصصة.

### قم بإعداد وسائل الإعلام وموارد اللاعب

تقوم العينة بتحميل الفيديو وصورة الملصق وملفات مظهر المشغل من مواقع محددة مسبقًا.

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

### قم بإنشاء التعليق التوضيحي للوسائط الغنية

```python
rich_media_annotation = ann.RichMediaAnnotation(
    page,
    ap.Rectangle(100, 500, 300, 600, True),
)
```

### قم بإرفاق المشغل المخصص والجلد والملصق والفيديو

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

### قم بتعيين سلوك التشغيل وحفظ ملف PDF

يتم تكوين التعليق التوضيحي كمحتوى فيديو ويتم تنشيطه عندما ينقر المستخدم عليه.

```python
rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO
rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK

rich_media_annotation.update()

page.annotations.append(rich_media_annotation)
document.save(outfile)
```

### مثال كامل

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

### حذف التعليقات التوضيحية للوسائط الغنية

يزيل سير العمل هذا جميع التعليقات التوضيحية للوسائط الغنية من الصفحة الأولى من PDF الحالي.

### افتح ملف PDF واجمع التعليقات التوضيحية للوسائط الغنية

```python
document = ap.Document(infile)
page = document.pages[1]

to_delete = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
]
```

### احذف التعليقات التوضيحية واحفظ المستند

```python
for annotation in to_delete:
    page.annotations.delete(annotation)

document.save(outfile)
```

### مثال كامل

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

## احصل على التعليقات التوضيحية للوسائط المتعددة

لفحص محتوى الوسائط المتعددة المخزن بالفعل في PDF، قم بتصفية مجموعة التعليقات التوضيحية لأنواع التعليقات التوضيحية للشاشة والصوت والوسائط الغنية.

### افتح المستند وحدد أنواع التعليقات التوضيحية المستهدفة

```python
document = ap.Document(infile)

target_types = {
    ann.AnnotationType.SCREEN,
    ann.AnnotationType.SOUND,
    ann.AnnotationType.RICH_MEDIA,
}
```

### طباعة مستطيلات التعليقات التوضيحية للوسائط المتعددة

```python
for annotation in document.pages[1].annotations:
    if annotation.annotation_type in target_types:
        print(f"{annotation.annotation_type} [{annotation.rect}]")
```

### مثال كامل

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

## موضوعات ذات صلة

- [استيراد التعليقات التوضيحية وتصديرها](/python-net/import-export-annotations/)
- [التعليقات التوضيحية التفاعلية](/python-net/interactive-annotations/)
- [التعليقات التوضيحية للتوصيف](/python-net/markup-annotations/)
- [التعليقات التوضيحية للأمان](/python-net/security-annotations/)
- [التعليقات التوضيحية للشكل](/python-net/shape-annotations/)
- [التعليقات التوضيحية المستندة إلى النص](/python-net/text-based-annotations/)
- [التعليقات التوضيحية للعلامة المائية](/python-net/watermark-annotations/)
