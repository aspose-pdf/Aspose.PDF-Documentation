---
title: Obtener y buscar imágenes en PDF
linktitle: Obtener y buscar imágenes
type: docs
weight: 40
url: /es/java/search-and-get-images-from-pdf-document/
description: Aprenda cómo buscar e inspeccionar imágenes en documentos PDF en Java.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Buscar e inspeccionar imágenes en archivos PDF con Java
Abstract: Este artículo muestra cómo buscar e inspeccionar imágenes en documentos PDF usando Aspose.PDF for Java. Cubre la lectura de la geometría de ubicación de la imagen, la detección del tipo de color, la extracción de texto alternativo y el cálculo de la resolución efectiva de la imagen a partir de los operadores de página.
---
Aspose.PDF for Java puede inspeccionar la información de ubicación de la imagen así como los datos de dibujo de nivel inferior.

## Obtener parámetros de ubicación de la imagen

Utiliza este ejemplo cuando necesites inspeccionar la geometría de la imagen y la resolución efectiva en una página.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Utilice [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para recopilar ubicaciones de imágenes.
1. Muestre el tamaño, las coordenadas y la resolución de cada imagen colocada.

```java
public static void extractImageParams(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("image width: " + imagePlacement.getRectangle().getWidth());
            System.out.println("image height: " + imagePlacement.getRectangle().getHeight());
            System.out.println("image LLX: " + imagePlacement.getRectangle().getLLX());
            System.out.println("image LLY: " + imagePlacement.getRectangle().getLLY());
            System.out.println("image horizontal resolution: " + imagePlacement.getResolution().getX());
            System.out.println("image vertical resolution: " + imagePlacement.getResolution().getY());
        }
    }
}
```

## Detectar tipos de color de imagen

Utilice este ejemplo cuando necesite contar imágenes en escala de grises y RGB en una página PDF.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Utilice [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para iterar sobre las imágenes de la página.
1. Lea el [`ColorType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/) de cada imagen y genere los totales.

```java
public static void extractImageTypesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        int grayscaled = 0;
        int rgb = 0;

        document.getPages().get_Item(1).accept(absorber);

        System.out.println("--------------------------------");
        System.out.println("Total Images = " + absorber.getImagePlacements().size());

        int imageCounter = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            ColorType colorType = imagePlacement.getImage().getColorType();
            if (colorType == ColorType.Grayscale) {
                grayscaled++;
                System.out.println("Image " + imageCounter + " is Grayscale...");
            } else if (colorType == ColorType.Rgb) {
                rgb++;
                System.out.println("Image " + imageCounter + " is RGB...");
            }
            imageCounter++;
        }

        System.out.println("--------------------------------");
        System.out.println("Grayscale Images = " + grayscaled);
        System.out.println("RGB Images = " + rgb);
    }
}
```

## Extraer texto alternativo de la imagen

Utilice este ejemplo cuando necesite inspeccionar el texto de accesibilidad asociado a las imágenes de la página.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Utilice [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para recopilar ubicaciones de imágenes.
1. Lea el texto alternativo de cada imagen y genere la salida.

```java
public static void extractImageAltText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            System.out.println("Name in collection: " + imagePlacement.getImage().getNameInCollection());
            List<String> lines = imagePlacement.getImage().getAlternativeText(document.getPages().get_Item(1));
            if (!lines.isEmpty()) {
                System.out.println("Alt Text: " + lines.get(0));
            } else {
                System.out.println("Alt Text: ");
            }
        }
    }
}
```

## Calcular la información de la imagen a partir de los operadores de página

Utilice este ejemplo cuando necesite derivar el tamaño y la resolución efectivos de la imagen a partir de los operadores de contenido de página de bajo nivel.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y recopile nombres de recursos de imagen.
1. Rastree el estado gráfico mientras se itera sobre los operadores de página.
1. Resuelva cada operación de dibujo de imagen y calcule sus dimensiones y resolución efectivas.

```java
public static void extractImageInformationFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int defaultResolution = 72;
        List<Matrix> graphicsState = new ArrayList<>();
        List<String> imageNames = Arrays.asList(document.getPages().get_Item(1).getResources().getImages().getNames());

        graphicsState.add(new Matrix(1, 0, 0, 1, 0, 0));

        for (Operator operator : document.getPages().get_Item(1).getContents()) {
            if (operator instanceof GSave) {
                graphicsState.add(new Matrix(graphicsState.get(graphicsState.size() - 1)));
            } else if (operator instanceof GRestore) {
                graphicsState.remove(graphicsState.size() - 1);
            } else if (operator instanceof ConcatenateMatrix concatenateMatrix) {
                Matrix current = graphicsState.get(graphicsState.size() - 1);
                graphicsState.set(graphicsState.size() - 1, current.multiply(concatenateMatrix.getMatrix()));
            } else if (operator instanceof Do doOperator) {
                if (imageNames.contains(doOperator.getName())) {
                    Matrix lastCtm = graphicsState.get(graphicsState.size() - 1);
                    int index = imageNames.indexOf(doOperator.getName()) + 1;
                    XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(index);

                    double scaledWidth = Math.sqrt(Math.pow(lastCtm.getA(), 2) + Math.pow(lastCtm.getB(), 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCtm.getC(), 2) + Math.pow(lastCtm.getD(), 2));

                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    String info = String.format(
                            "%s image %s (%.2f:%.2f): res %.2f x %.2f",
                            inputFile,
                            doOperator.getName(),
                            scaledWidth,
                            scaledHeight,
                            resHorizontal,
                            resVertical);
                    System.out.println(info);
                }
            }
        }
    }
}
```
