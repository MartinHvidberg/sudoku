
import sdk_hums
import sdk_prmu

lol_u = [
        ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e'],
        ['E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I'],
        ['j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n'],
        ['N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R'],
        ['s', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w'],
        ['W', 'x', 'X', 'y', 'Y', 'z', 'Z', 'Ø', '1'],
        ['2', '3', '4', '5', '6', '7', '8', '9', '!'],
        ['"', '#', '{', '}', '&', '*', '/', '(', ')'],
        ['=', '?', '+', '-', '@', '£', '$', '[', ']']
    ]

sdka = sdk_hums.SdkHums("")
sdka.set_matrix(lol_u)  # Brute force overwrite the matrix with this (invalid) contents
sdkb = sdk_prmu.flip_v(sdka)
sdkc = sdk_prmu.flip_h(sdka)
sdkd = sdk_prmu.turn_l(sdka)
sdke = sdk_prmu.turn_r(sdka)

print(f"ref: {sdka.dump_str()}")
print(f"flv: {sdkb.dump_str()}")
print(f"flh: {sdkc.dump_str()}")
print(f"trl: {sdkd.dump_str()}")
print(f"trr: {sdke.dump_str()}")

print("\n*** Permute ***")
sdk = sdk_hums.SdkHums('763128459924567831851934276418295367275643198639781542342876915186359724597412683')
print(f"dump_in: {sdk.dump_str()}")

sdk_prm = sdk_prmu.permute(sdk, str_to="0823456719")
print(f"dump_pu: {sdk_prm.dump_str()}")


