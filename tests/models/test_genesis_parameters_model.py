import json
from datetime import datetime

from pccontext.models.genesis_parameters_model import GenesisParameters


def test_genesis_params_from_blockfrost(blockfrost_get_genesis_json):
    genesis_params = GenesisParameters.from_json(blockfrost_get_genesis_json)
    assert genesis_params.active_slots_coefficient == float(
        blockfrost_get_genesis_json["active_slots_coefficient"]
    )
    assert genesis_params.update_quorum == int(
        blockfrost_get_genesis_json["update_quorum"]
    )
    assert genesis_params.max_lovelace_supply == int(
        blockfrost_get_genesis_json["max_lovelace_supply"]
    )
    assert genesis_params.network_magic == int(
        blockfrost_get_genesis_json["network_magic"]
    )
    assert genesis_params.epoch_length == int(
        blockfrost_get_genesis_json["epoch_length"]
    )
    assert genesis_params.system_start == int(
        blockfrost_get_genesis_json["system_start"]
    )
    assert genesis_params.slots_per_kes_period == int(
        blockfrost_get_genesis_json["slots_per_kes_period"]
    )
    assert genesis_params.slot_length == int(blockfrost_get_genesis_json["slot_length"])
    assert genesis_params.max_kes_evolutions == int(
        blockfrost_get_genesis_json["max_kes_evolutions"]
    )
    assert genesis_params.security_param == int(
        blockfrost_get_genesis_json["security_param"]
    )


def test_genesis_params_from_cli(cli_get_shelley_genesis_json):
    genesis_params = GenesisParameters.from_json(cli_get_shelley_genesis_json)
    assert genesis_params.active_slots_coefficient == float(
        cli_get_shelley_genesis_json["activeSlotsCoeff"]
    )


def test_genesis_params_from_koios(koios_get_genesis_json):
    genesis_params = GenesisParameters.from_json(koios_get_genesis_json)
    assert genesis_params.network_magic == int(
        koios_get_genesis_json[0]["networkmagic"]
    )
    assert genesis_params.network_id == koios_get_genesis_json[0]["networkid"]
    assert genesis_params.active_slots_coefficient == float(
        koios_get_genesis_json[0]["activeslotcoeff"]
    )
    assert genesis_params.update_quorum == int(
        koios_get_genesis_json[0]["updatequorum"]
    )
    assert genesis_params.max_lovelace_supply == int(
        koios_get_genesis_json[0]["maxlovelacesupply"]
    )
    assert genesis_params.epoch_length == int(koios_get_genesis_json[0]["epochlength"])
    assert genesis_params.system_start == int(koios_get_genesis_json[0]["systemstart"])
    assert genesis_params.slots_per_kes_period == int(
        koios_get_genesis_json[0]["slotsperkesperiod"]
    )
    assert genesis_params.slot_length == int(koios_get_genesis_json[0]["slotlength"])
    assert genesis_params.max_kes_evolutions == int(
        koios_get_genesis_json[0]["maxkesrevolutions"]
    )
    assert genesis_params.security_param == int(
        koios_get_genesis_json[0]["securityparam"]
    )
    assert genesis_params.alonzo_genesis == json.loads(
        koios_get_genesis_json[0]["alonzogenesis"]
    )
    assert isinstance(genesis_params.alonzo_genesis, dict)


def test_to_dict(fake_genesis_parameters):
    result = fake_genesis_parameters.to_dict()
    expected = {
        "activeSlotsCoeff": fake_genesis_parameters.active_slots_coefficient,
        "updateQuorum": fake_genesis_parameters.update_quorum,
        "maxLovelaceSupply": fake_genesis_parameters.max_lovelace_supply,
        "networkMagic": fake_genesis_parameters.network_magic,
        "epochLength": fake_genesis_parameters.epoch_length,
        "systemStart": fake_genesis_parameters.system_start,
        "slotsPerKESPeriod": fake_genesis_parameters.slots_per_kes_period,
        "slotLength": fake_genesis_parameters.slot_length,
        "maxKESEvolutions": fake_genesis_parameters.max_kes_evolutions,
        "securityParam": fake_genesis_parameters.security_param,
    }
    assert result == expected


def test_to_json(blockfrost_get_genesis_json):
    genesis_params = GenesisParameters(**blockfrost_get_genesis_json)
    result = genesis_params.to_json()
    expected = json.dumps(
        {
            "activeSlotsCoeff": blockfrost_get_genesis_json["active_slots_coefficient"],
            "epochLength": blockfrost_get_genesis_json["epoch_length"],
            "maxKESEvolutions": blockfrost_get_genesis_json["max_kes_evolutions"],
            "maxLovelaceSupply": blockfrost_get_genesis_json["max_lovelace_supply"],
            "networkMagic": blockfrost_get_genesis_json["network_magic"],
            "securityParam": blockfrost_get_genesis_json["security_param"],
            "slotLength": blockfrost_get_genesis_json["slot_length"],
            "slotsPerKESPeriod": blockfrost_get_genesis_json["slots_per_kes_period"],
            "systemStart": blockfrost_get_genesis_json["system_start"],
            "updateQuorum": blockfrost_get_genesis_json["update_quorum"],
        }
    )
    assert result == expected
