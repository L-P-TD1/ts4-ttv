import event_testing
import services
from event_testing.tests import _TunableTestSetBase, TunableTestVariant, TestSetInstance
from sims4.resources import Types
from sims4.tuning.instances import HashedTunedInstanceMetaclass
from TravelToVenue.TestSets.TD1_TravelToVenue_TestSet_Pack import TD1TravelToVenuePackTest


class TD1TravelToVenueTunableTestSet(_TunableTestSetBase, is_fragment=True):

    def __init__(self, **kwargs):
        TunableTestVariant.TEST_VARIANTS['pack_test'] = TD1TravelToVenuePackTest.TunableFactory
        super().__init__(test_locked_args={}, **kwargs)


class TD1TravelToVenueTestSetInstance(TestSetInstance):

    INSTANCE_TUNABLES = {'test': TD1TravelToVenueTunableTestSet()}
