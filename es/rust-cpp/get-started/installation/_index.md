---
title: Cómo instalar Aspose.PDF para Rust mediante C++
linktitle: Instalación
type: docs
weight: 20
url: /es/rust-cpp/installation/
description: Esta sección muestra una descripción del producto e instrucciones para instalar Aspose.PDF for Rust por tu cuenta.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guía de instalación de Aspose.PDF for Rust
Abstract: La guía de instalación de Aspose.PDF for Rust via C++ proporciona instrucciones paso a paso para instalar y configurar la biblioteca para su uso en proyectos Rust con integración C++. Cubre varios métodos de instalación, incluyendo la configuración manual y el uso de gestores de paquetes como NuGet. La guía también describe los requisitos del sistema, las dependencias y los pasos de configuración necesarios para garantizar una integración sin problemas en los entornos de desarrollo. Esta documentación ayuda a los desarrolladores a comenzar a crear, leer y manipular documentos PDF en Rust a través de C++ de manera efectiva.
SoftwareApplication: rust-cpp
---

## Instalación

### Instalación desde el sitio web de Aspose

Este paquete incluye un archivo grande que se almacena como un archivo bzip2.

1. **Descargar** el archivo **Aspose.PDF for Rust via C\u002B\u002B** del sitio web oficial de Aspose.
   La versión más reciente (más actual) está listada en la parte superior y se descarga por defecto cuando haces clic en el botón **Download**.
   Se recomienda usar esta última versión. Sólo descargue una versión anterior si es necesario.
   Ejemplo: `Aspose.PDF-for-Rust-via-CPP-25.6.zip`

   El formato del nombre de archivo del archivo es: `Aspose.PDF-for-Rust-via-CPP-YY.M.zip`, donde:
   - `YY` = últimos dos dígitos del año (p.ej., `25` para 2025)
   - `M` = número de mes de `1` a `12`

2. **Extraer** el archivo a tu directorio elegido `{path}` usando una herramienta adecuada:

   - En Linux/macOS:

     ```bash
     unzip Aspose.PDF-for-Rust-via-CPP-YY.M.zip -d {path}
     ```

   - En Windows, use la extracción incorporada del Explorador o cualquier herramienta de descompresión (7-Zip, WinRAR).

3. **Agregar** la biblioteca como dependencia en tu proyecto Rust. Puedes hacerlo de dos maneras:

   - **Usando la línea de comandos:**

     ```bash
     cargo add asposepdf --path {path}/asposepdf
     ```

   - **Edición manual `Cargo.toml`:**
     Abre el proyecto de `Cargo.toml` y añada lo siguiente bajo `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { path = "{path}/asposepdf" }
     ```

4. **Compila tu proyecto** (`cargo build`). En la primera compilación, la biblioteca dinámica apropiada para su plataforma será extraída automáticamente de la `.bz2` archivar en el `lib` carpeta y vinculada a tu proyecto.

**Notas**

- El script de compilación intenta crear un **enlace simbólico** a la biblioteca en su directorio de salida (p. ej., `target/debug/`).
- Para **Linux y macOS**, también debe seguir el [Configuración de tiempo de ejecución](#runtime-configuration) sección a continuación para garantizar que el ejecutable pueda encontrar la biblioteca en tiempo de ejecución.
- Todo `.bz2` los archivos tienen correspondiente `.sha256` archivos de suma de verificación. Si falta una suma de verificación o es inválida, la compilación fallará.

### Instalación desde GitHub

Este paquete incluye bibliotecas nativas precompiladas ("`.dll`, `.so`, `.dylib`) que se almacenan como comprimidos `.bz2` archivos dentro del repositorio de GitHub.

1. **Agregar** la biblioteca como dependencia en tu proyecto Rust. Puedes hacerlo de dos maneras:

   - **Usando la línea de comandos:**

     ```bash
     cargo add asposepdf --git https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git
     ```

   - **Edición manual `Cargo.toml`:**

     Abre el proyecto de `Cargo.toml` y añada lo siguiente bajo `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git" }
     ```

    > **Nota:** Para usar una versión de lanzamiento específica, puedes especificar una etiqueta:
    >
    > ```toml
    > asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git", tag = "v1.26.1" }
    > ```

2. **Compila tu proyecto** (`cargo build`). En la primera compilación, la biblioteca dinámica apropiada para su plataforma será extraída automáticamente de la `.bz2` archivar en el `lib` carpeta y vinculada a tu proyecto.

**Notas**

- No necesitas descargar ni extraer manualmente ningún archivo - todo está incluido en el repositorio de GitHub.
- El script de compilación intenta crear un **enlace simbólico** a la biblioteca en su directorio de salida (p. ej., `target/debug/`).
- Para **Linux y macOS**, también debe seguir el [Configuración de tiempo de ejecución](#runtime-configuration) sección a continuación para garantizar que el ejecutable pueda encontrar la biblioteca en tiempo de ejecución.
- Todo `.bz2` los archivos tienen coincidencia `.sha256` archivos de suma de verificación. La suma de verificación se verifica antes de desempaquetar.
- Si la verificación de la suma de verificación falla o el archivo está ausente, la compilación fallará con un error detallado.

### Instalación desde crates.io

Este paquete está disponible en [crates.io](https://crates.io/crates/asposepdf). 
Debido a limitaciones de tamaño, el crate publicado no incluye las bibliotecas binarias nativas (`.dll`, `.so`, o `.dylib`).
Puedes obtener las bibliotecas nativas requeridas ya sea del archivo de distribución oficial (ver [Instalación desde el sitio web de Aspose](#installation-from-aspose-website)) o desde el repositorio de GitHub (ver [Instalación desde GitHub](#installation-from-github)).
El script de compilación localizará, verificará y extraerá la biblioteca nativa apropiada de un archivo comprimido .bz2 durante el proceso de compilación.

1. **Agregar** la biblioteca como dependencia en tu proyecto Rust. Puedes hacerlo de dos maneras:

   - **Usando la línea de comandos:**

     ```bash
     cargo add asposepdf
     ```

   - **Edición manual `Cargo.toml`:**

     Abre el proyecto de `Cargo.toml` y añada lo siguiente bajo `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = "1.26.1"
     ```

2. **Establecer la ruta** al directorio que contiene las bibliotecas nativas y descargar los archivos requeridos:

   - **Establecer la variable de entorno `ASPOSE_PDF_LIB_DIR`** para apuntar a la carpeta donde colocarás el nativo `.bz2` archivos, su `.sha256` archivos de suma de verificación, y las bibliotecas nativas extraídas (`.dll`, `.so`, `.dylib`, y también para Windows `.lib`):

     - En Linux/macOS:

       ```bash
       export ASPOSE_PDF_LIB_DIR=/path/to/lib
       ```

     - En Windows (Símbolo del sistema):

       ```cmd
       set ASPOSE_PDF_LIB_DIR=C:\path\to\lib
       ```

     - En Windows (PowerShell):
     
       ```powershell
       $env:ASPOSE_PDF_LIB_DIR = "C:\path\to\lib"
       ```

**Nota sobre ASPOSE_PDF_LIB_DIR**

El `ASPOSE_PDF_LIB_DIR` la variable de entorno define el directorio de trabajo para el script de compilación. Se usa **solo durante la compilación** para localizar, verificar y extraer los archivos de biblioteca nativos. Configurar esta variable **no** agrega automáticamente el directorio a la ruta de búsqueda de bibliotecas en tiempo de ejecución de su sistema (ver [Configuración de tiempo de ejecución](#runtime-configuration)).

  - **Descargar lo necesario** `.bz2` archivos** y archivos de suma de verificación del repositorio de GitHub [`lib/` carpeta](https://github.com/aspose-pdf/aspose-pdf-rust-cpp/tree/main/lib) y **colócalos** en la carpeta establecida en `ASPOSE_PDF_LIB_DIR`:

  - Para **Linux x64**, descargar:
    - `libAsposePDFforRust_linux_amd64.so.bz2`
    - `libAsposePDFforRust_linux_amd64.so.bz2.sha256`

  - Para **macOS x86_64**, descarga:
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2`
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2.sha256`

  - Para **macOS arm64**, descarga:
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2`
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2.sha256`

  - Para **Windows x64**, descargar:
    - `AsposePDFforRust_windows_amd64.dll.bz2`
    - `AsposePDFforRust_windows_amd64.dll.bz2.sha256`
    - `AsposePDFforRust_windows_amd64.lib` (biblioteca de importación nativa, sin comprimir)

**Nota:** Necesitas descargar manualmente estos archivos desde GitHub y colocarlos en el directorio indicado por `ASPOSE_PDF_LIB_DIR`.  
El script de compilación desempaquetará automáticamente las bibliotecas nativas del `.bz2` archivos en la primera compilación.

3. **Compilar** tu proyecto (`cargo build`). En la primera compilación, la biblioteca nativa que coincida con su plataforma se extraerá automáticamente de la `.bz2` archivar y vincular a su proyecto.

**Importante:** Para **Linux y macOS**, también debe seguir la [Configuración de tiempo de ejecución](#runtime-configuration) sección a continuación para garantizar que el ejecutable pueda encontrar la biblioteca en tiempo de ejecución.

**Notas**

- El `ASPOSE_PDF_LIB_DIR` la variable se usa **solo durante el proceso de compilación** para localizar y extraer los archivos.
- El script de compilación intenta crear un **enlace simbólico** a la biblioteca extraída en su directorio de salida (por ejemplo, `target/debug/`).
- Debe proporcionar la carpeta que contiene el `.bz2` y `.sha256` archivos por separado, ya que estos archivos binarios no se distribuyen a través de crates.io.
- Si el archivo requerido falta o la suma de verificación falla, la compilación fallará con un error detallado.
- Los mismos archivos binarios utilizados para la instalación a través de GitHub o del sitio web de Aspose pueden reutilizarse aquí.

## Inicio rápido

Todos los fragmentos de código están contenidos en el [fragmento](https://onedrive.live.com/examples).