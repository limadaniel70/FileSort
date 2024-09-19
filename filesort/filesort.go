package main

import (
	"fmt"
	"os"
	"path/filepath"
)

var fileExtensions = map[string]string{
	".txt":  "TextFiles",
	".jpg":  "Images",
	".jpeg": "Images",
	".png":  "Images",
	".pdf":  "Documents",
	".docx": "Documents",
}

func sortFiles(directory string) {
	var organizedFiles int

	filepath.Walk(directory, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			fmt.Printf("Erro ao acessar o caminho %q: %v\n", path, err)
			return err
		}

		if info.IsDir() {
			return nil
		}

		ext := filepath.Ext(info.Name())
		if category, ok := fileExtensions[ext]; ok {
			newDir := filepath.Join(directory, category)
			err := os.MkdirAll(newDir, os.ModePerm)
			if err != nil {
				fmt.Printf("Erro ao criar o diretório %q: %v\n", newDir, err)
				return err
			}

			newPath := filepath.Join(newDir, info.Name())
			err = os.Rename(path, newPath)
			if err != nil {
				fmt.Printf("Permissão negada: não foi possível mover o arquivo %q\n", path)
				return err
			}

			organizedFiles++
		}

		return nil
	})

	fmt.Printf("Arquivos organizados: %d\n", organizedFiles)
}

func main() {
	directory := "."
	sortFiles(directory)
}
