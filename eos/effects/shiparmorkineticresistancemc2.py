# Used by:
# Ship: Mimir
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Cruiser").level
    fit.ship.boostItemAttr("armorKineticDamageResonance", ship.getModifiedItemAttr("shipBonusMC2") * level)
