import FWCore.ParameterSet.Config as cms
process = cms.Process("Filter")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
# process.load('Configuration.StandardSequences.MagneticField_0T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

process.source = cms.Source("PoolSource",
fileNames = cms.untracked.vstring(
# Run 234029
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/029/00000/00097CE4-A2B2-E411-8FEB-02163E011D8A.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/029/00000/0049B70A-8EB2-E411-8979-02163E011D1C.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/029/00000/004DEB4A-9DB2-E411-AB38-02163E011D06.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/029/00000/00D04605-A5B2-E411-A496-02163E0129F4.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/029/00000/00D21ADC-A2B2-E411-8861-02163E011D57.root',

# Runs >= 234500
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/500/00000/3E97325D-17B6-E411-8908-02163E011D59.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/500/00000/703041ED-16B6-E411-ABFE-02163E0123AE.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/521/00000/2ECA3A0A-17B6-E411-9363-02163E011890.root',

# Run 234542
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/542/00000/08AE2B88-94B6-E411-8782-02163E0124F8.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/542/00000/08EDDCA1-8FB6-E411-8FFB-02163E012301.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/542/00000/0A61047C-90B6-E411-8F2A-02163E012A44.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/542/00000/0A81A278-94B6-E411-B795-02163E012502.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/542/00000/14688E77-90B6-E411-AB89-02163E012042.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/542/00000/1863DB7C-94B6-E411-AEF5-02163E0126FC.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/542/00000/1ADCB5AC-91B6-E411-8C49-02163E01240C.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/542/00000/1CB1F17D-94B6-E411-968A-02163E0129F4.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/542/00000/2006D077-90B6-E411-BD92-02163E01217E.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/542/00000/20F012D7-95B6-E411-89F2-02163E0121FD.root',

# Run 234556
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/234/556/00000/',

# Run 234929
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/238/929/00000/0CA4E30D-09D3-E411-9E55-02163E01357F.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/238/929/00000/42E56E63-01D3-E411-92D6-02163E012237.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/238/929/00000/4C129CB8-01D3-E411-9BE9-02163E0139BF.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/238/929/00000/5408400B-08D3-E411-802B-02163E01391D.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/238/929/00000/60B1A811-07D3-E411-B80C-02163E011DF0.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/238/929/00000/7079A196-01D3-E411-A7E7-02163E013567.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/238/929/00000/ACB8C60C-09D3-E411-A012-02163E011DE6.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/238/929/00000/B07A490F-09D3-E411-ACA3-02163E012433.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/238/929/00000/B2590513-09D3-E411-955A-02163E01379E.root',
# '/store/express/Commissioning2015/ExpressCosmics/FEVT/Express-v1/000/238/929/00000/F0FA540D-08D3-E411-B72F-02163E01368B.root',

# Run 234484
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/020BA8F9-17F3-E411-B392-02163E0133E3.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/0E3330F9-3DF3-E411-8378-02163E0128CB.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/101FDFC7-09F3-E411-AEB6-02163E0122E9.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/10CC5B2E-3DF3-E411-949B-02163E01395B.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/14FE02CC-17F3-E411-8C8C-02163E01358B.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/16C92324-0EF3-E411-AD67-02163E01381C.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/2056654C-3AF3-E411-BD66-02163E011A2A.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/22570961-1FF3-E411-9CCA-02163E0137CE.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/22C9594F-0FF3-E411-AF49-02163E01380A.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/2406AD45-0EF3-E411-B0C7-02163E0133A8.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/24671EC9-17F3-E411-8EE6-02163E013392.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/2A51612D-12F3-E411-A4CF-02163E01384F.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/2C5D8BFF-0CF3-E411-AC96-02163E01390C.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/2CECEC3B-1CF3-E411-8FA3-02163E0133E2.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/2ED32C3A-22F3-E411-93EA-02163E013459.root',
'/store/express/Commissioning2015/ExpressPhysics/FEVT/Express-v1/000/243/484/00000/32B37C91-19F3-E411-B3A1-02163E0133BB.root',


# RelVal ZMM
# '/store/relval/CMSSW_7_3_0/RelValZMM_13/GEN-SIM-RECO/MCRUN2_73_V9_71XGENSIM_FIXGT-v1/00000/0AC5D8E4-5DA2-E411-8B1D-0025905B8590.root',
# '/store/relval/CMSSW_7_3_0/RelValZMM_13/GEN-SIM-RECO/MCRUN2_73_V9_71XGENSIM_FIXGT-v1/00000/AC3E5968-5CA2-E411-B77E-0025905938AA.root',
# '/store/relval/CMSSW_7_3_0/RelValZMM_13/GEN-SIM-RECO/MCRUN2_73_V9_71XGENSIM_FIXGT-v1/00000/C69684E2-5DA2-E411-ADF0-0025905964C2.root',

# My Filtered Rootfiles
# 'file:MyFilteredEvents_234029_Test.root'
# 'file:/afs/cern.ch/user/p/piet/public/ForFrancesca/MyFilteredEvents_234029_BX0_NoDTSegments.root'
)
)
process.Out = cms.OutputModule("PoolOutputModule",
SelectEvents = cms.untracked.PSet(
SelectEvents = cms.vstring('path')
),
# fileName = cms.untracked.string ("MyFilteredEvents_234029_RPC_BX0_DT_BX0.root")
# fileName = cms.untracked.string ("MyFilteredEvents_234029_RPC_BX1_DT_BX0.root")
# fileName = cms.untracked.string ("MyFilteredEvents_234029_RPC_BX0_DT_BX1.root")
# fileName = cms.untracked.string ("MyFilteredEvents_234029_BX0_PointingMuons.root")
# fileName = cms.untracked.string ("MyFilteredEvents_234029_BX0_NoDTSegments.root")
# fileName = cms.untracked.string ("MyFilteredEvents_234029_BX0_NoRPCRechits.root")
# fileName = cms.untracked.string ("MyFilteredEvents_234029_Test.root")
# fileName = cms.untracked.string ("MyFilteredEvents_234500.root")
# fileName = cms.untracked.string ("MyFilteredEvents_234542_BX0_NoDTSegments.root")
fileName = cms.untracked.string ("MyFilteredEvents_238929_PointingMuons.root")
)
process.filter = cms.EDFilter('MyOutOfTimeRPCTriggerFilter',
Debug                = cms.untracked.bool(False),
GTReadoutRcd         = cms.InputTag("gtDigis"),
GMTReadoutRcd        = cms.InputTag("gtDigis" ),
STAMuonTrackCollectionLabel = cms.InputTag("standAloneMuons",""),         # UpdatedAtVtx
TrackerTrackCollectionLabel = cms.InputTag("ctfWithMaterialTracksP5",""), # globalMuons or globalCosmicMuons or globalCosmicMuons1Leg
# TrackerTrackCollectionLabel = cms.InputTag("generalTracks",""), # for normal PP / ZMM MC
SelectBX             = cms.untracked.bool(False),
# config 0 :: RPC in bx=0, DT in bx=0
bxRPC                = cms.untracked.int32(0),
bxDT                 = cms.untracked.int32(0),
# config 1 :: RPC in bx=1, DT in bx=0
# bxRPC              = cms.untracked.int32(1),
# bxDT               = cms.untracked.int32(0),
# config 2 :: RPC in bx=0, DT in bx=1
# bxRPC              = cms.untracked.int32(0),
# bxDT               = cms.untracked.int32(1),
AnalyzeTRK           = cms.untracked.bool(False),
SelectTRK            = cms.untracked.bool(False),
SelectAND            = cms.untracked.bool(False),  # selectBX && selectTRK
SelectOR             = cms.untracked.bool(True),   # selectBX || selectTRK, one has to choose one or the other
SelectNoDTSegments   = cms.untracked.bool(True),   # from here on selection is independent
SelectNoRPCRechits   = cms.untracked.bool(False),
SelectDTbutNoRPCTrig = cms.untracked.bool(False),
SelectRPCbutNoDTTrig = cms.untracked.bool(False),
SelectTRKTrack       = cms.untracked.bool(False),
SelectMUOTrack       = cms.untracked.bool(False),
SelectSTATrack       = cms.untracked.bool(True),
DoFilter             = cms.untracked.bool(True),
# RootFileName       = cms.untracked.string("MyFilteredHistograms_234029_RPC_BX0_DT_BX0_.root"),
# RootFileName       = cms.untracked.string("MyFilteredHistograms_234029_RPC_BX1_DT_BX0_.root"),
# RootFileName       = cms.untracked.string("MyFilteredHistograms_234029_RPC_BX0_DT_BX1_.root"),
# RootFileName       = cms.untracked.string("MyFilteredHistograms_234029_BX0_PointingMuons.root"),
# RootFileName       = cms.untracked.string("MyFilteredHistograms_234029_BX0_NoDTSegments.root")
# RootFileName       = cms.untracked.string("MyFilteredHistograms_234029_BX0_NoRPCRechits.root"),
# RootFileName       = cms.untracked.string("MyFilteredHistograms_234029_Test.root"),
# RootFileName       = cms.untracked.string("MyFilteredHistograms_234500.root"),
# RootFileName       = cms.untracked.string("MyFilteredHistograms_234542_BX0_NoDTSegments.root")
RootFileName       = cms.untracked.string("MyFilteredHistograms_243484_PointingMuons.root"),
)
process.path = cms.Path(process.filter)
process.end = cms.EndPath(process.Out)
