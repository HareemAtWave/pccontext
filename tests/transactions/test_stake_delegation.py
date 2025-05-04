from pycardano import Address, PoolKeyHash, StakeSigningKey, StakeVerificationKey

from pccontext.transactions.stake_delegation import stake_delegation


def test_stake_delegation_success(chain_context):
    """
    Test successful stake address registration.
    """
    sk = StakeSigningKey.generate()
    vk = StakeVerificationKey.from_signing_key(sk)
    address = Address.from_primitive(
        "addr1x8nz307k3sr60gu0e47cmajssy4fmld7u493a4xztjrll0aj764lvrxdayh2ux30fl0ktuh27csgmpevdu89jlxppvrswgxsta"
    )
    pool_id = "dd0b5f0c8db566f23b3ac2ffd63c4b5ea2afe1d2ca7c9810b1827e2f"
    transaction = stake_delegation(chain_context, vk, pool_id, address)
    assert transaction.valid is True
    assert (
        transaction.transaction_body.certificates[0].stake_credential.credential
        == vk.hash()
    )
    assert transaction.transaction_body.certificates[0].pool_keyhash == PoolKeyHash(
        bytes.fromhex(pool_id)
    )
