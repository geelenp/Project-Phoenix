package main

import (
	"fmt"

	"gitlab.com/bboehmke/sunny"
)

func main() {

	conn, err := sunny.NewConnection("")
	if err != nil {
		panic(err)
	}

	fmt.Println("Zoeken naar SMA apparaten...")

	devices := conn.SimpleDiscoverDevices("0000")

	fmt.Printf("%d apparaat(en) gevonden\n\n", len(devices))

	for _, d := range devices {

		fmt.Printf("=====================================================\n")
		fmt.Printf("IP      : %s\n", d.Address().IP)
		fmt.Printf("Serial  : %d\n", d.SerialNumber())
		fmt.Printf("Meter   : %v\n", d.IsEnergyMeter())

		values, err := d.GetValues()
		if err != nil {
			fmt.Println("GetValues fout:", err)
			continue
		}

		fmt.Printf("Aantal waarden : %d\n\n", len(values))

		for id, value := range values {
			fmt.Printf("%-40v %v\n", id, value)
		}

		fmt.Println()
	}
}
