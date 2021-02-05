```java
    public static void ConvertPostscriptToPDFAvdanced() {
        
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "svg_test.pdf").toString();
        String svgDocumentFileName = Paths.get(_dataDir.toString(), "car.svg").toString();
        
        SvgLoadOptions option = new SvgLoadOptions();
        option.setAdjustPageSize(true);

        Document pdfDocument = new Document(svgDocumentFileName, option);
        pdfDocument.getPages().get_Item(1).getPageInfo().getMargin().setTop(0);
        pdfDocument.getPages().get_Item(1).getPageInfo().getMargin().setLeft(0);
        pdfDocument.getPages().get_Item(1).getPageInfo().getMargin().setBottom(0);
        pdfDocument.getPages().get_Item(1).getPageInfo().getMargin().setRight(0);
        pdfDocument.save(pdfDocumentFileName);
    }
}
```