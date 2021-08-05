---
title: PDF 3D Annotation 
linktitle: 3D Annotation
type: docs
weight: 140
url: /androidjava/3d-annotation/
description: The PDF 3D Annotation in the document uses to represent volumetric image models on the page. Check code snippet to resolve this task.
lastmod: "2021-06-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

In PDF documents, you can view and manage high-quality 3D content created with 3D CAD or 3D modeling software and embedded in the PDF document. Can rotate 3D elements in all directions as if you were holding them in your hands.

Why do you need a 3D display of images at all?

Over the past few years, tech has made huge breakthroughs in all areas thanks to 3D printing. 3D printing technologies can be applied to teach technological skills in construction, mechanical engineering, design as the main tool. These technologies thanks to the emergence of personal printing devices can contribute to the introduction of new forms of organization of the educational process, increase motivation, and formation of the necessary competencies of graduates
and teachers.

The main task of 3D modeling is the idea of a future object or object because, in order to release an object, you need an understanding of its design features in all detail for successive regeneration in industrial design or architecture.

## Add 3D Annotation

3D annotation is added using a model created in the U3D format with Aspose.PDF for Java

1. Create a new [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Load the data of the desired 3D model (in our case "Ring.u3d") to create [PDF3DContent](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/PDF3DContent)
1. Create [3dArtWork](https://apireference.aspose.com/pdf/java/com.aspose.pdf/PDF3DArtwork) object and link it to the document and 3DContent
1. Tune pdf3dArtWork object:

    - 3DLightingScheme - (we will set  `CAD` in example)
    - 3DRenderMode - (we will set `Solid` in example)
    - Fill `ViewArray`, create at least one [3D View](https://apireference.aspose.com/pdf/java/com.aspose.pdf/PDF3DView) and add it to array.

1. Set 3 basic parameters in annotation:
    - the `page` on which the annotation will be placed,
    - the `rectangle`, inside which the annotation,
    - and the `3dArtWork` object.
1. For a better presentation of the 3D object, set the Border frame
1. Set the default view (for example - TOP)
1. Add some additional parameters: name, preview poster etc.
1. Add Annotation to the [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page)
1. Save the result

## Example

Please check the following code snippet to add 3D Annotation.

```java
    public class Example3DAnnotation 
    {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";
    public static void Add3dAnnotation()
    {
    // Load the PDF file
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
    pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));        
    pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));
        
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.getPages().add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
    pdf3dAnnotation.setDefaultViewIndex(1);
    pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
    pdf3dAnnotation.setName("Ring.u3d");
    //set preview image if needed
    //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
    document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

    document.save(_dataDir+"sample_3d.pdf");
    }
}  
```

This code example showed us such a model:

![3D Annotation demo](3d_demo.png)
