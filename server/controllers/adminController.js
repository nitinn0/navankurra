export const adminDashboard = async (req, res, next) => {
  try {
    res.json({
      stats: {
        students: 12500,
        courses: 24,
        certificates: 9840,
        contactQueries: 68
      },
      activeCourses: 7,
      platformHealth: 'healthy'
    });
  } catch (error) {
    next(error);
  }
};

export const adminCourses = async (req, res, next) => {
  try {
    res.json({ data: [] });
  } catch (error) {
    next(error);
  }
};
