---
title: Configuración de tiempo de ejecución Aspose.PDF para Rust vía C++
linktitle: Configuración de tiempo de ejecución
type: docs
weight: 100
url: /es/rust-cpp/runtime-configuration/
description: Las aplicaciones Rust que dependen de bibliotecas dinámicas nativas—como Aspose.PDF—requieren una configuración correcta de la ruta de tiempo de ejecución para funcionar adecuadamente en sistemas Linux y macOS
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Configurando RPATH para Aspose.PDF nativo para Rust
Abstract: Al trabajar con bibliotecas dinámicas nativas en Rust, el enlace correcto en tiempo de ejecución es esencial para garantizar que su aplicación pueda localizar las dependencias requeridas. En Linux y macOS, el cargador dinámico del sistema no busca automáticamente el directorio del ejecutable a menos que RPATH esté configurado explícitamente. Este artículo explica cómo configurar RPATH para que su aplicación Rust pueda localizar correctamente la biblioteca nativa Aspose.PDF en tiempo de ejecución. Cubre la configuración a nivel de proyecto usando Cargo, la configuración basada en el entorno con RUSTFLAGS y las opciones de instalación a nivel del sistema, junto con notas sobre el comportamiento en Windows.
SoftwareApplication: rust-cpp
---

> Este es un requisito estándar al usar bibliotecas dinámicas nativas en Rust.

En Linux y macOS, el cargador dinámico del sistema no busca automáticamente el directorio del ejecutable a menos que RPATH esté configurado. Para garantizar que su aplicación pueda encontrar la biblioteca nativa de Aspose.PDF en tiempo de ejecución, debe configurar el **RPATH** (Ruta de búsqueda en tiempo de ejecución).

Nuestro script de compilación extrae la biblioteca y trata de crear un enlace simbólico a ella en su directorio de salida (p. ej., `target/debug/`). Para que el ejecutable lo encuentre, elija una de las siguientes opciones:

## Opción 1: Configuración a nivel de proyecto (Recomendado)

Crear una carpeta llamada `.cargo` en el directorio raíz de tu proyecto (si no existe) y crea un archivo llamado `config.toml` dentro de él:

```toml
[target.'cfg(target_os = "linux")']
rustflags = ["-C", "link-arg=-Wl,-rpath,$ORIGIN"]

[target.'cfg(target_os = "macos")']
rustflags = ["-C", "link-arg=-Wl,-rpath,@loader_path"]
```

## Opción 2: Variable de entorno RUSTFLAGS

Construye tu proyecto con la siguiente bandera:

```bash
# Linux
RUSTFLAGS="-C link-arg=-Wl,-rpath,\$ORIGIN" cargo build

# macOS
RUSTFLAGS="-C link-arg=-Wl,-rpath,@loader_path" cargo build
```

## Opción 3: Instalación a nivel del sistema (No recomendada para desarrollo)

Si prefieres instalar la biblioteca globalmente:

* **Linux:** Copiar el `.so` archivo a `/usr/local/lib` y ejecutar `sudo ldconfig`.
* **macOS:** Copiar el `.dylib` archivo a `/usr/local/lib`.

> **Windows**
> Normalmente no se requiere ninguna acción porque la biblioteca está ubicada en la misma carpeta que el `.exe`. Alternativamente, puede agregar el directorio que contiene el `.dll` a su sistema `PATH` variable de entorno.