import fme
import fmeobjects


class FeatureProcessor(object):
    """Template Class Interface:
    When using this class, make sure its name is set as the value of the 'Class to Process Features'
    transformer parameter.
    """

    def __init__(self):
        """Base constructor for class members."""
        pass
        
    def has_support_for(self, support_type: int):
        """This method is called by FME to determine if the PythonCaller supports Bulk mode,
        which allows for significant performance gains when processing large numbers of features.
        Bulk mode cannot always be supported. 
        More information available in transformer help.
        """
        return support_type == fmeobjects.FME_SUPPORT_FEATURE_TABLE_SHIM
  
    def input(self, feature: fmeobjects.FMEFeature):
        """This method is called for each feature which enters the PythonCaller. 
        Processed input features can be emitted from this method using self.pyoutput().
        If knowledge of all input features is required for processing, then input features should be 
        cached to a list instance variable and processed using group processing or in the close() method.
        """
        self.pyoutput(feature)

    def close(self):
        """This method is called once all the FME Features have been processed from input()."""
        pass

    def process_group(self):
        """This method is called by FME for each group when group processing mode is enabled.
        This implementation should reset any instance variables used for the next group. 
        Bulk mode should not be enabled when using group processing. 
        More information available in transformer help.
        """
        pass